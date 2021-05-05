from django.db import models
class MyUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True)