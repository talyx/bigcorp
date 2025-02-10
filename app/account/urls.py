from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.shortcuts import render
from . import views

app_name = "account"

urlpatterns = [
    #Registration and verification
    path("register", views.register_user, name="register"),
    path(
        "email-verification-sent/",
        lambda request: render(request, "account/email/email-verification-sent.html"),
        name="email-verification-sent",
    ),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    #Dashboard
    path("dashboard", views.dashboard_user, name="dashboard"),
    path("profile-management", views.profile_user, name="profile-management"),
    path('delete-user/', views.delete_user, name='delete-user'),
    
    #Password Reset
    path(
        'passwrod-reset/', auth_views.PasswordResetView.as_view(
            template_name='account/password/password_reset.html',
            success_url=reverse_lazy('account:password-reset-done'),
            email_template_name='account/password/password_reset_email.html',
        ),
        name='password-reset',
    ),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password/password_reset_done.html',
    ), name = 'password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='account/password/password_reset_confirm.html',
        success_url=reverse_lazy('account:password-reset-complete'),
    ), name='password-reset-confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password/password_reset_complete.html',
    ), name='password-reset-complete'),
    
]
