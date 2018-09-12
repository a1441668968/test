from django.contrib import admin
from .models import Group, Host, Module, Args

# Register your models here.
admin.site.register(Group)
admin.site.register(Host)
admin.site.register(Module)
admin.site.register(Args)
