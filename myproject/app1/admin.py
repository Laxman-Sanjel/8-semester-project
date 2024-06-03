from django.contrib import admin
from .models import Suppliers
from .models import Further_Treatment
from .models import Rescue
from .models import Product
from .models import Sales
from .models import Order

# Register your models here.
from.models import *
admin.site.register(Suppliers)
admin.site.register(Product)
admin.site.register(Rescue)
admin.site.register(Further_Treatment)
admin.site.register(Sales)
admin.site.register(Order)
