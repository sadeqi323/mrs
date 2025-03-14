from django.contrib import admin
from .models import CalIn,CalOut,Token
# Register your models here.
admin.site.register(CalIn)
admin.site.register(CalOut)
admin.site.register(Token)
