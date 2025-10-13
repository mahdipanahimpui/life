from django.urls import path
from . import views


app_name = 'extra'

urlpatterns = [
    path('about_us/', views.AboutUsView.as_view(), name='about_us'),
    path('contact_us/', views.ContactUsView.as_view(), name='contact_us'),
    path('active-notification/', views.ActiveNotificationView.as_view(), name='active_notification'),
    path('terms/', views.TermsView.as_view(), name='terms'),

]
