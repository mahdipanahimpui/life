# accounts/middleware.py
from django.shortcuts import redirect
from django.urls import reverse
from .models import UserToken

class AutoAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user.is_authenticated:
            refresh_token = request.COOKIES.get('refresh_token')
            
            if refresh_token:
                try:
                    token = UserToken.objects.get(refresh_token=refresh_token)
                    
                    if token.is_valid():
                        from django.contrib.auth import login
                        login(request, token.user)
                
                except UserToken.DoesNotExist:
                    pass
        
        response = self.get_response(request)
        return response