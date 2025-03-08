from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password dont match! ')
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you can change password <a href=\"../password/\">this form</a>.")

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'full_name', 'password', 'last_login')


class UserRegistrationForm(forms.Form):
    full_name = forms.CharField(label='نام کامل', label_suffix=': ', widget=forms.TextInput(
        attrs={'placeholder': 'نام کامل خود را وارد نمایید'}))
    phone = forms.CharField(label='شماره تلفن', label_suffix=': ', max_length=11, widget=forms.TextInput(
        attrs={'placeholder': 'شماره تلفن خود را وارد نمایید'}))
    email = forms.EmailField(label='ایمیل', label_suffix=': ', widget=forms.EmailInput(
        attrs={'placeholder': 'ایمیل خود را وارد نمایید'}))
    password1 = forms.CharField(min_length=8, label='رمز عبور', label_suffix=': ', widget=forms.PasswordInput(
        attrs={'placeholder': 'رمز عبور خود را وارد نمایید'}))
    password2 = forms.CharField(min_length=8, label='تایید رمز عبور', label_suffix=': ', widget=forms.PasswordInput(
        attrs={'placeholder': 'رمز عبور خود را مجدداً وارد نمایید'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('این ایمیل قبلا توسط کاربر دیگری ثبت شده! ')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        user = User.objects.filter(full_name=full_name).exists()
        if user:
            raise ValidationError('این نام قبلا توسط کاربر دیگری ثبت شده! ')
        return full_name

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')

        if p1 and p2 and p1 != p2:
            raise ValidationError('رمز عبور ها باید مشابه باشند! ')


class UserLoginForm(forms.Form):
    phone = forms.CharField(label='شماره تلفن', label_suffix=': ', max_length=11, widget=forms.TextInput(
        attrs={'placeholder': 'شماره تلفن خود را وارد نمایید'}))
    password = forms.CharField(min_length=8, label='رمز عبور', label_suffix=': ', widget=forms.PasswordInput(
        attrs={'placeholder': 'رمز عبور خود را وارد نمایید'}))


