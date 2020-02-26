from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    path(r'password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='supplier/auth/password_reset_done.html'), name='password_reset_done'),
    path(r'reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='supplier/auth/password_reset_complete.html'), name='password_reset_complete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)