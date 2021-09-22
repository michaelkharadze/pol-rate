from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from users.forms import UserPasswordResetForm, UserPasswordSetForm

urlpatterns = [
    path('', include('politicians.urls')),
    path('register/', user_views.register, name="register"),
    path('login/', user_views.CustomLoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
#     path('password-reset/',
#          auth_views.PasswordResetView.as_view(template_name='users/password_reset.html', form_class=UserPasswordResetForm),
#          name="password_reset"),
    path('password-reset/',
         user_views.password_reset_request,
         name="password_reset"),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html', form_class=UserPasswordSetForm),
         name="password_reset_confirm"),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name="password_reset_complete"),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
]
