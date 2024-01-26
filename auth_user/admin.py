from django.contrib import admin
from .models import UserAccount, UserAddress,Follow


admin.site.register(UserAccount)
admin.site.register(UserAddress)
admin.site.register(Follow)