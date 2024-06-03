from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime
user=settings.AUTH_USER_MODEL

# Create your models here.
class Suppliers(models.Model):
    name=models.CharField(max_length=220)
    email=models.EmailField(max_length=100)
    address=models.TextField()
    phone=models.IntegerField()
    gst_no=models.IntegerField()
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=220)
    origin=models.CharField(max_length=100)
    suppliers=models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    gender=models.CharField(max_length=770)
    date=models.DateTimeField(auto_now_add=True,null=True)
    image= models.ImageField(upload_to="img/images",blank=True,null=True)
    quantity=models.IntegerField()
    price=models.IntegerField()
    lifespan=models.PositiveIntegerField()
    color=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    profit=models.IntegerField(default=0)

    def __str__(self):
      return self.name


class Rescue(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)  # Assuming it's a string
    location = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    status = models.CharField(max_length=20,default='pending',null=False)

    def __str__(self):
      return self.name

class Further_Treatment(models.Model):
    pet_id = models.TextField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    assign_doctor = models.CharField(max_length=100)
    condition = models.CharField(max_length=10, choices=[('Normal', 'Complicated'), ('Normal', 'Complicated')])
    discharge_date = models.DateField()
    Rescue_id=models.ForeignKey(Rescue,on_delete=models.CASCADE)

    def __str__(self):   
       return self.pet_id
    
class Sales(models.Model):
    breed = models.ForeignKey(Product, on_delete=models.CASCADE)
    profit_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
       return self.breed
METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Khalti", "Khalti"),
    ("Esewa", "Esewa"),
)
class Order(models.Model):
   image = models.ImageField(upload_to='order_images/', blank=True, null=True)
   name=models.CharField(max_length=220)
   user=models.ForeignKey(User, on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField()
   price = models.DecimalField(max_digits=10, decimal_places=2)
   address = models.TextField()
   phone = models.CharField(max_length=15)
   pincode = models.CharField(max_length=110)
   order_status = models.CharField(max_length=50,default="Order Pending")
   payment_method = models.CharField(max_length=20,default="Cash On Delivery")
   payment_completed = models.BooleanField(default=False, null=True, blank=True)
   date = models.DateTimeField(default=datetime.datetime.today)
   pid = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)
#    product_id = models.PositiveIntegerField()
   
   def __str__(self):
       return self.name
   

