from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from .models import Notification


# ---------------------------------------------------------
class AboutUsView(View):
    template_name = 'extra/about_us.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
        

# ---------------------------------------------------------
class ContactUsView(View):
    template_name = 'extra/contact_us.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

# -----------------------------------------------------------------
# ---------------------------------------------------------
class TermsView(View):
    template_name = 'extra/terms.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


# ----------------------------------------------------------------
class ActiveNotificationView(View):
    def get(self, request, *args, **kwargs):
        try:
            notification = Notification.objects.filter(is_active=True).first()
            
            if notification:
                data = {
                    'exists': True,
                    'title': notification.title,
                    'message': notification.message,
                    'id': notification.id
                }
            else:
                data = {'exists': False}
                
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'exists': False})
