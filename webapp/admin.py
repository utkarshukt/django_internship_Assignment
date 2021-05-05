from django.contrib import admin
from .models import Advisor,Customer,Book
# Register your models here.
admin.site.register(Advisor)
admin.site.register(Customer)
admin.site.register(Book)
