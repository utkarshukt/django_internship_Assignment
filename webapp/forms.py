from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Advisor, Book


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AdvisorForm(ModelForm):
    class Meta:
        model = Advisor
        fields = '__all__'


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
