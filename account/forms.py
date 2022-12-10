from django.forms import ModelForm
from users.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class RegUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
