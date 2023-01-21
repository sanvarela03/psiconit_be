from django.contrib import admin

# For model registration
from .models.user import User
from .models.account import Account

admin.site.register(User)
admin.site.register(Account)
