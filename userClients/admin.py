from django.contrib import admin
from . import models

admin.site.register(models.UserClient)
admin.site.register(models.UserSharesData)
admin.site.register(models.UserCurrency)