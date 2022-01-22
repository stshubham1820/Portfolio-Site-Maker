from django.contrib import admin
# Register your models here.
from .models import *
# Register your models here.
class user(admin.ModelAdmin):
    list_display = ('UserName','Password','Email')
    def __str__(self) -> str:
        return self.user
admin.site.register(User,user)
