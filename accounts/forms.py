from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Wrong Password")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    name = forms.CharField(max_length=200)
    facebook = forms.CharField(max_length=300)
    twitter = forms.CharField(max_length=300)
    instagram = forms.CharField(max_length=300)
    img_url = forms.CharField(max_length=1000)
    about = forms.CharField(widget=forms.Textarea, max_length=500)
    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'email',
            'about',
            'facebook',
            'twitter',
            'instagram',
            'password',
            'password2'
        ]

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Both password should match')

        return password2
