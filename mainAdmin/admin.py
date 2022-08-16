from email.headerregistry import Group
from django.contrib import admin

from .models import Menus, Rest_admin, Waiter
admin.site.site_header = "EasyFoods"


admin.site.register(Rest_admin)
admin.site.register(Waiter)
admin.site.register(Menus)
