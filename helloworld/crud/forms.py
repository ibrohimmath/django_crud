from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password_confirm = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'image', 'first_name', 'last_name', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_password_confirm(self):
        """Ensure that the two password fields match."""
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return password_confirm

    def save(self, commit=True):
        """Override the save method to set the password properly."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password
        if commit:
            user.save()
        return user
