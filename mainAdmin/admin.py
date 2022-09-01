from email.headerregistry import Group
from django.contrib import admin

from .models import Cuisine, Menu, Shop, Table, Waiter
admin.site.site_header = "EasyFoods"


admin.site.register(Shop)
admin.site.register(Waiter)
admin.site.register(Menu)
admin.site.register(Cuisine)
admin.site.register(Table)