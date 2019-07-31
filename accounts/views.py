from django.contrib import (
    messages,
    auth,
)
from django.contrib.auth import (
    login,
    get_user_model,
    logout,
)
from django.shortcuts import (
    render,
    redirect,
)
from django.contrib.auth.forms import (
    UserChangeForm,
    PasswordChangeForm,
)
from django.contrib.auth import update_session_auth_hash
from django.views.generic import View
from django.views.generic.base import (
    TemplateView,
    TemplateResponseMixin,
    ContextMixin,
)

from django.core.paginator import (
    EmptyPage,
    PageNotAnInteger,
    Paginator,
)
from .forms import (
    UserCreationForm,
    UserLoginForm,
    EditProfileForm,
    # SendMessageForm,
    # RegistrationForm,
)

from django.http import (
    HttpResponseRedirect,
    HttpResponse,
)
from .models import Profile
# from django.contrib.auth.models import User
# from datetime import datetime
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
User = get_user_model()


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_account.html', args)


@login_required(login_url='/accounts/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been updated!')
            return redirect('profile')
        else:
            return redirect('accounts/change_password.html')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'You are now registered and can log in')
        return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username_ = form.cleaned_data.get('username')
        user_obj = User.objects.get(username__iexact=username_)
        login(request, user_obj)
        messages.success(request, 'You are now logged in')
        return redirect('profile')

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

# def send_message(request, *args, **kwargs):
#     form = BaseWriteForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Your message has been sent!')
#         return redirect('profile')
