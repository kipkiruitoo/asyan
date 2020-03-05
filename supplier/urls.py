from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .forms import EmailValidationOnForgotPassword
from . import views

app_name = 'supplier'

urlpatterns = [
    path('', views.index, name='supply_home'),

    url('login/', views.user_login, name='user_login'),
    url('register/', views.register_user, name='register_user'),
    url('logout/', views.loguser_out, name='logout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),

    path(r'password_reset', auth_views.PasswordResetView.as_view(template_name='supplier/auth/password_reset_form.html',
                                                                 subject_template_name='supplier/auth/password_reset_subject.txt',
                                                                 email_template_name='supplier/auth/password_reset_email.html',
                                                                 form_class=EmailValidationOnForgotPassword), name='password_reset'),
    path(r'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='supplier/auth/password_reset_confirm.html'), name='password_reset_confirm'),

    # =============================================================================================

    path('tenders/all', views.tenders_all_view, name='all_tenders'),
    path('tenders/<int:pk>', views.tenders_detail_view, name='tender_detail_n_apply'),
# change pass
    path('editprofile/', views.editprofile, name='editprofile'),
    path('changepassword/', views.changepassword, name='changepassword'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)