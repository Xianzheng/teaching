from django.contrib import admin
from .models import UserDB
from .models import UserInfo
from .models import BlogInfo
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(UserDB)
admin.site.register(BlogInfo)