from django.db import models


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    desc=models.TextField(max_length=120)
    state=models.CharField(max_length=20)
    date=models.DateField()

    def __str__(self):
        return self.name

class Product(models.Model):
    catg= [
    ('GRAINS', 'Grains & Pulses'),
    ('SNACKS', 'Snacks'),
    ('BREAKFAST', 'Breakfast'),
    ('VEG', 'Fruit&Veg'),
    ('DAIRY', 'Dairy')]
    name=models.CharField(max_length=20)
    id=models.AutoField
    desc=models.TextField(max_length=150)
    date=models.DateField()
    category=models.CharField(max_length=20, default="", choices=catg)
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="polls/images", default="")
 
    def __str__(self):
        return self.name
    

class Order(models.Model):
    ord_id=models.AutoField
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    address=models.TextField(max_length=200)
    state=models.CharField(max_length=20)
    date=models.DateField()
    pin=models.IntegerField()
    items_json = models.CharField(max_length=5000, default="")

    def __str__(self):
        return self.name
    
    
