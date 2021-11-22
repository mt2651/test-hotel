# # from django.shortcuts import render
# # from django.shortcuts import redirect, render
# # from django.urls import reverse
# # from account.forms import CustomUserCreationForm, RegistrationForm

# # # Create your views here.

# # def register(request):
# #     form = RegistrationForm()
# #     if request.method == 'POST':
# #         form = RegistrationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             signup_succes = reverse('signup_success')
# #             redirect(signup_succes)
# #     return render(request, 'signup.html', {'form': form})

# # def Signup_success(request):
# #     return render(request, 'signup_success.html')

# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.contrib.sites.shortcuts import get_current_site
# from django.shortcuts import render, redirect
# from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string

# from account.forms import SignUpForm
# from account.tokens import account_activation_token


# @login_required
# def home(request):
#     return render(request, 'home.html')


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()

#             current_site = get_current_site(request)
#             subject = 'Activate Your MySite Account'
#             message = render_to_string('account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             user.email_user(subject, message)

#             return redirect('account_activation_sent')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


# def account_activation_sent(request):
#     return render(request, 'account_activation_sent.html')


# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.profile.email_confirmed = True
#         user.save()
#         login(request, user)
#         return redirect('home')
#     else:
#         return render(request, 'account_activation_invalid.html')


from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from account.forms import SignUpForm, LoginForm
from django.contrib.auth.views import LoginView
# from ac.forms import RegisterForm, LoginForm


# @login_required
def home(request):
    return render(request, 'index.html')
    # return HttpResponse(render(request,'index.html'))


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            # user.profile.birth_date = form.cleaned_data.get('birth_date')
            # user.customuser.account_role = form.cleaned_data.get('account_role')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)