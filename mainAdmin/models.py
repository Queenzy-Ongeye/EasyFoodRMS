from secrets import choice
from django.db import models

# Create your models here.
class Shop(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self) :
            return super().get_queryset() .filter(status= 'published' )
            
    name = models.CharField(max_length=25, blank=True)
    tagline = models.CharField(max_length=25, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

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
    waiter_rest = models.ForeignKey("Shop", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} , {self.waiter_rest}'
class Menu(models.Model):
    name = models.CharField(max_length=255, blank=True)
    descrpition = models.CharField(max_length=255, blank=True)
    shop_menu = models.ForeignKey("Shop", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} "

class Cuisine(models.Model):
    MEALS = (
        ("BRK", "Breakfast"),
        ("LNCH", "Lunch"),
        ("DNNR", "Dinner"),
        ("Snk", "Snack"),
        ("DRK", "Drinks")
    )
    food = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(default=0, blank=True)
    cuisine_menu = models.ForeignKey("Menu", null=True, on_delete=models.CASCADE)
    mealtime = models.CharField(max_length=255, blank=True, choices= MEALS)

    def __str__(self):
        return f"{self.food} ---------------{self.price}"

class Table(models.Model):
    TABLE = (
        ("Small", "2 People Seats"),
        ("4small", "4 People Seats"),
        ("4-6small", "4-6 People Seats"),
        ("8-10 Large", "8-10 People Seats"),
        ("Large", "8-12 People Seats"),
    )

    tableSize = models.CharField(max_length=100, blank=True, choices= TABLE)
    capacity = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f"{self.tableSize}"
