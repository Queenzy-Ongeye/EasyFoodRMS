from pyexpat import model
from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=25, blank=True)
    tagline = models.CharField(max_length=25, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class Waiter(models.Model):
    GENDER = (
        ("F", "Female"),
        ("M", "Male"),
        ("Non-B", "Non-Binary"),
    )
    name = models.CharField(max_length=25, blank=True)
    gender = models.CharField(max_length=25, blank=True, choices= GENDER)
    numberOfTable = models.IntegerField(default=0)
    waiter_rest = models.ForeignKey("Rest_admin", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} , {self.waiter_rest}'
class Menus(models.Model):
    MENULIST = (
        ("BRKFAST", "Breakfast"),
        ("LNCH", "Lunch"),
        ("DNNR", "Dinner"),
        ("SNCK", "Snacks"),
        ("DRK", "Drinks"),
    )

    menu = models.CharField(max_length=25, blank=True, choices= MENULIST)
    add_menu = models.CharField(max_length=25, blank=True)
    set_price = models.IntegerField(default=0, null=True)
    rest= models.ForeignKey("Rest_admin", null=True,on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.menu} "

