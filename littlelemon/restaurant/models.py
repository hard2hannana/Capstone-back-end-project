from django.db import models


# Create your models here.
class Booking(models.Model):
    full_name = models.CharField(max_length=200)
    number_of_guests = models.SmallIntegerField(default=6)
    booking_date = models.DateTimeField()
    

    def __str__(self): 
        return self.full_name

class Menu(models.Model):
   title = models.CharField(max_length=200) 
   price = models.DecimalField(max_digits=10, decimal_places=2)
   inventory = models.SmallIntegerField(default=5) 

   def __str__(self):
      return self.title
