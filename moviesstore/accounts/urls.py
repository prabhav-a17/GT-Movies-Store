# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),

    # Password Reset URLs:
    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/forgot_password/reset_password.html',
            from_email='jimbolimbo365@gmail.com'
        ),
        name='reset_password'
    ),
    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/forgot_password/password_reset_sent.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/forgot_password/password_reset_form.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/forgot_password/password_reset_done.html'
        ),
        name='password_reset_complete'
    ),
]
