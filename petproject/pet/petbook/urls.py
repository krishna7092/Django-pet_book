from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('booking.html', views.booking, name='booking'),
    path('reset_password_complete/booking.html', views.booking, name='booking'),
    path('index.html', views.index, name='index'),
    path('register', views.register, name='register'),
    path('reset_password_complete/login', views.index, name='index'),
    path('reset_password_complete/index.html', views.index, name='index'),
    path('reset_password_complete/register', views.register, name='register'),
    path('login', views.login, name='login1'),
    path('logout', views.logout, name='logout1'),
    path('bookpet', views.bookpet, name='bookpet'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),




]
