from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('verify/', views.UserRegisterVerifyCodeView.as_view(), name='verify_code'),
    path('auto-login/', views.AutoLoginView.as_view(), name='auto_login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]