from django.views import View
from .forms import UserRegistrationForm, VerifyCodeForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from utils.utils import send_otp_code
from .models import OtpCode, User, UserToken
from django.contrib import messages
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import login, logout
import random


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/login.html'
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            random_code = random.randint(10000, 99999)
            phone_number = form.cleaned_data['phone_number']
            send_otp_code(phone_number, random_code)
            OtpCode.objects.create(phone_number=phone_number, code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': phone_number
            }

            # messages.success(request, 'we send you a code', 'success')
            
            return redirect('accounts:verify_code')
        return render(request, self.template_name, {'form': form})
    


class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm
    template_name = 'accounts/otp-verification.html'

    def get(self, request):
        form = self.form_class
        context = {
            'form': form,
            'phone_number': request.session['user_registration_info']['phone_number']
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user_session = request.session['user_registration_info']
        phone_number = user_session['phone_number']
        
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            code_instance = OtpCode.objects.filter(code=cd['code'], phone_number=phone_number)
            if code_instance.exists():
                user, created = User.objects.get_or_create(phone_number=phone_number)

                code_instance.delete()

                refresh_token = UserToken.generate_refresh_token()
                expires_at = timezone.now() + timedelta(days=365)
                    
                token, created = UserToken.objects.get_or_create(
                    user=user,
                    defaults={
                        'refresh_token': refresh_token,
                        'expires_at': expires_at
                    }
                )
                    
                if not created:
                    token.refresh_token = refresh_token
                    token.expires_at = expires_at
                    token.save()
                
                # لاگین کاربر
                login(request, user)
                    
                # تنظیم کوکی
                response = redirect('home:home')
                response.set_cookie(
                    'refresh_token',
                    refresh_token,
                    max_age = settings.USER_COOKIE_AGE,
                    httponly=True,
                    secure=request.is_secure()
                )
                    
                # messages.success(request, 'احراز هویت با موفقیت انجام شد', 'success')
                return response
            
            else:
                messages.error(request, 'کد تأیید نامعتبر یا منقضی شده است', 'error')
                return redirect('accounts:verify_code')
                    

        return redirect('home:home')
        
                    
class AutoLoginView(View):
    def get(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        
        if refresh_token:
            try:
                token = UserToken.objects.get(refresh_token=refresh_token)
                
                if token.is_valid():
                    login(request, token.user)
                    # messages.success(request, 'ورود خودکار با موفقیت انجام شد', 'success')
                    return redirect('home:home')
                else:
                    messages.info(request, 'لطفاً مجدداً وارد شوید', 'info')
                
            except UserToken.DoesNotExist:
                messages.info(request, 'لطفاً وارد شوید', 'info')
        
        return redirect('accounts:user_register')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        
        if refresh_token:
            try:
                token = UserToken.objects.get(refresh_token=refresh_token)
                token.delete()
            except UserToken.DoesNotExist:
                pass
        
        logout(request)
        response = redirect('home:home')
        response.delete_cookie('refresh_token')
        messages.success(request, 'خروج با موفقیت انجام شد')
        return response