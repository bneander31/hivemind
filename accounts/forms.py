from django import forms
from django.contrib.auth.forms import (
    ReadOnlyPasswordHashField,
)
from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from django.core.validators import RegexValidator
from .models import USERNAME_REGEX

User = get_user_model()
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username / Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        the_user = authenticate(username=username, password=password)
        if not the_user:
            raise forms.ValidationError('Invalid credentials')

        return super(UserLoginForm, self).clean(*args, **kwargs)



class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with cms's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'tel', 'street_address', 'city', 'state',
                  'picture', 'is_staff', 'is_active', 'is_admin',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]



class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'zipcode',
            'tel',
            'street_address',
            'city',
            'state',
            'picture',
            # 'password',
        )

