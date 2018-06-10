from django.contrib import admin
from .models import BlogUser, EmailVerifyRecord

# Register your models here.

admin.site.register(BlogUser)
admin.site.register(EmailVerifyRecord)