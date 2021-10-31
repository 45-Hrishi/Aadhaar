from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'accounts'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('accountdetail/',views.Accountdetail,name='accountdetail'),
    
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html', success_url = reverse_lazy('accounts:password_reset_done')), name="password_reset"),

    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name="password_reset_done"),

    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name="password_reset_confirm"),

    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name="password_reset_complete"),

    path('update_address/<int:pk>/', views.AddressUpdateView.as_view(template_name = 'accounts/address_update.html'),name='address_update'),

    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutView, name="logout"),
]
