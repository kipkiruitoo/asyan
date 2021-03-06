from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from accounts.forms import LoginForm, PasswordChangeForm ,UserChangeForm
from accounts.models import User
from .models import Company, Tender, TenderApplication
from .forms import UserRegisterForm, CompanyForm
from .tokens import account_activation_token


def index(request):
    template = 'supplier/index.html'
    tender_list = Tender.objects.filter(is_active=True).order_by('-rating')[:10]
    return render(request, template, {'tenders': tender_list})


# ==================== Auth ======================

def user_login(request):
    template = 'supplier/auth/login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            if not User.objects.filter(email=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username doest not exists.'
                })
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/pp/')
            else:
                return render(request, template, {
                    'form': form
                })
        else:
            return render(request, template, {
                'form': form,
            })
    else:
        form = LoginForm()

    return render(request, template, {'form': form})


def register_user(request):
    template = 'supplier/auth/user_registration.html'
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form2 = CompanyForm(request.POST)
        if form.is_valid() and form2.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'A user with such username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'A user with such email already exists.'
                })
            else:

                # create user
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                # create company
                company = Company()
                company.user = user
                company.name = form2.cleaned_data['name']
                company.address = form2.cleaned_data['address']
                company.phone = form2.cleaned_data['phone']
                company.save()

                # send email address
                current_site = get_current_site(request)
                mail_subject = '( Asyana ) Activate your account.'
                message = render_to_string('supplier/auth/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                return render(request, 'supplier/auth/registration_email_sent.html', {})
        else:
            return render(request, template, {
                'form': form,
                'company_form': form2
            })
        # No post data availabe, let's just show the page.
    else:
        form = UserRegisterForm()
        form2 = CompanyForm(initial={'user': request.user})

    return render(request, template, {'form': form, 'company_form': form2})


def activate(request, uidb64, token):
    template = 'supplier/auth/acc_activate_done.html'
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request, template,
                      {'message': 'Thank you for your email confirmation. Now you can login your account.'})
    else:
        return render(request, template, {'error': 'Activation link is invalid!'})


def loguser_out(request):
    logout(request)
    return HttpResponseRedirect('/pp/')


# ========================================================================

def tenders_all_view(request):
    template = 'supplier/tenders_all.html'
    tender_list = Tender.objects.filter(is_active=True)
    return render(request, template, tender_list)


def tenders_detail_view(request, pk):
    template = 'supplier/tenders_detail.html'
    user = request.user
    tender = Tender.objects.get(id=pk)
    if request.method == 'POST':  # apply for this tender
        if not request.user.is_authenticated:
            return redirect('/pp/login/')
        my_tender = TenderApplication(user=user, tender=tender, discount_terms=request.POST.get('discount_terms', None))
        my_tender.save()
        return render(request, 'supplier/application_received.html')
    return render(request, template, {'tender': tender})


# supplier change pass word
def editprofile(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ("Your Profile Updated"))
            return redirect('home')
    else:
        form = UserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'supplier/editprofile.html', context)


# user password change form

def changepassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Your Password Changed", extra_tags='green')
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'supplier/changepassword.html', context)

