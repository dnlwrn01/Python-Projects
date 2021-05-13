from django.contrib import admin

# Register your models here.
from .models import Transaction, Account

# Register your models here.
admin.site.register(Transaction)
admin.site.register(Account)

