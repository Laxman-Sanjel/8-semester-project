from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group, Permission
from django.contrib import auth
from .models import Suppliers
from .models import Product
from .models import Rescue
from django.db.models import Max
from .models import Further_Treatment
from django.http import HttpResponse
from pathlib import Path
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from cart.cart import Cart
from .models import Sales
from .models import Order
from django.shortcuts import get_object_or_404
from django.views.generic import View
import requests                     
from django.urls import reverse

# Create your views here.

def SignupPage(request):
    if request.method=='POST':
       uname=request.POST.get('username')
       email=request.POST.get('email')
       pass1=request.POST.get('password1')
       pass2=request.POST.get('password2')
       if pass1!=pass2:
           return HttpResponse("Your password and confirm password is not same!")
       else:
         my_user=User.objects.create_user(uname,email,pass1)
         my_user.save()
       return HttpResponse("user has been created Successsfully!")
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=auth.authenticate(request,username=username,password=pass1)
        
        if user is not None and user.is_staff==True:
            messages.success(request,'welcome User')
            return redirect('AdminDashboard')
        elif user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username and Password are incorrect!")
    return render(request,'login.html')

def HomePage(request):
    return render(request,'UserDashboard/home.html')

@login_required(login_url="login")
def LogoutPage(request):
    logout(request)
    return redirect('login')  

def StaffPage(request):
    return render(request,'AdminDashboard.html')

def Show_SuppliersPage(request):
    s=Suppliers.objects.all()             # pylint: disable=no-member
    return render(request,'Suppliers/Add_Suppliers.html',{'s':s})

def del_page(request,id):
    dele=Suppliers.objects.get(id=id)      # pylint: disable=no-member
    dele.delete()
    messages.success(request,'Data successfully deleted!')
    return redirect('Show_Suppliers') 

def SuppliersPage(request):
 if request.method=='POST':
       name=request.POST.get('name')
       email=request.POST.get('email')
       contact=request.POST.get('contact')
       gst_no=request.POST.get('gst')
       address=request.POST.get('address')
       ss=Suppliers()
       ss.name=name
       ss.email=email
       ss.phone=contact
       ss.gst_no=gst_no
       ss.address=address
       ss.save()
       messages.success(request,'data inserted successfully!')
       return redirect('Show_Suppliers') 
 
 #for product
def Product_list(request):
    p=Product.objects.all()                                     # pylint: disable=no-member
    return render(request,'Products/list_items.html',{'p':p})   # pylint: disable=no-member

def Product_Form(request):
    s=Suppliers.objects.all()                                 # pylint: disable=no-member
    return render(request,'Products/Addform.html',{'s':s})   # pylint: disable=no-member

def Add_Product(request):
 if request.method=='POST':
       bname=request.POST.get('bname')
       origin=request.POST.get('origin')
       gender=request.POST.get('gender')
       date=request.POST.get('date')
       quantity=request.POST.get('quantity')
       price = float(request.POST.get('price'))
       profit_percentage = float(request.POST.get('profit'))
       profit=(profit_percentage / 100) * price + price
       image=request.FILES['image']
       lifespan=request.POST.get('lifespan')
       color=request.POST.get('color')
       type=request.POST.get('type')
       suppliers=request.POST.get('suppliers')
       supplier = Suppliers.objects.get(pk=suppliers)    # pylint: disable=no-member

       p=Product()
       p.name=bname
       p.origin=origin
       p.gender=gender
       p.date=date
       p.suppliers=supplier
       p.quantity=quantity
       p.price=price
       p.image=image
       p.lifespan=lifespan
       p.color=color
       p.type=type
       p.profit=profit
       p.save()
       messages.success(request,'data inserted successfully!')
       return redirect('productslist')
 
def Del_Product(request,id):
    dele=Product.objects.get(id=id)      # pylint: disable=no-member
    dele.delete()
    messages.success(request,'Data successfully deleted!')
    return redirect('productslist') 

    # for rescue  
def Rescue_Page(request):
    return render(request,'UserDashboard/Rescue.html')

def Add_RescueForm(request):
 if request.method=='POST':
       name=request.POST.get('name')
       number=request.POST.get('number')
       location=request.POST.get('location')
       message=request.POST.get('message')
       image=request.POST.get('image')
       status=request.POST.get('status')      
       r=Rescue()
       r.name=name
       r.number=number
       r.location=location
       r.message=message
       r.image=image
       r.status=status
       r.save()
       messages.success(request,'Your Data successfully Send!')
       return redirect('Rescue') 

def Rescue_list(request):
    R=Rescue.objects.filter(status='pending')        # pylint: disable=no-member
    return render(request,'AdminDash/Rescue_list.html',{'R':R}) 

def Request_Accept(request):
    accept=Rescue.objects.filter(status='Accept')    # pylint: disable=no-member
    return render(request,'AdminDash/Req_Accepted.html',{'accept':accept})

def Rescue_Action(request,id):
    Rr=Rescue.objects.get(id=id)        # pylint: disable=no-member
    return render(request,'AdminDash/ActionForm.html',{'Rr':Rr})

def Treatment(request):
  if request.method=='POST':
       pet_id=request.POST.get('pet_id')
       assign_doctor=request.POST.get('assign_doctor')
       gender=request.POST.get('gender')
       condition=request.POST.get('condition')
       discharge_date=request.POST.get('discharge_date') 
       f=Further_Treatment()    
       f.pet_id=pet_id
       f.assign_doctor=assign_doctor
       f.gender=gender
       f.condition=condition
       f.discharge_date=discharge_date
       f.save()
       messages.success(request,'Your Data successfully Inserted!')
       return redirect('Treatment') 

def Update_RescueForm(request,id):
 if request.method=='POST':
       name=request.POST.get('name')
       number=request.POST.get('number')
       location=request.POST.get('location')
       message=request.POST.get('message')
       image=request.POST.get('image') 
       status=request.POST.get('status')
       r=Rescue.objects.get(id=id)           # pylint: disable=no-member
       r.name=name
       r.number=number
       r.location=location
       r.message=message
       r.image=image
       r.status=status
       r.save()
       messages.success(request,'Your Data successfully Updated!')
       return redirect('Rescue_list_items')

def Product_Page(request):
    pp=Product.objects.all()               # pylint: disable=no-member
    return render(request,'UserDashboard/Product.html',{'pp':pp})

def Pet_Details(request,id):
    details=Product.objects.get(id=id)       # pylint: disable=no-member
    return render(request,'UserDashboard/Pet_Details.html',{'details':details})  
 
@login_required(login_url="login")
def cart_add(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)    # pylint: disable=no-member
    pid = Product.objects.get(id=id)        # pylint: disable=no-member
    cart.add(product=product)
    return render(request,'UserDashboard/add_to_cart.html',{'product':product,'pid':pid}) 

@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)   # pylint: disable=no-member
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)    # pylint: disable=no-member
    cart.add(product=product)
    return redirect('cart_detail')

@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)    # pylint: disable=no-member
    cart.decrement(product=product)
    return redirect('cart_detail')

@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')

@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'UserDashboard/add_to_cart.html')

def Sales_Product (request):
    sp = Product.objects.all()   # pylint: disable=no-member
    sl = Sales.objects.all()     # pylint: disable=no-member
    return render(request,'AdminDash/Sales.html',{'sp':sp,'sl':sl})

def add_sales(request):
    if request.method == 'POST':
        breed_id = request.POST.get('breed')
        profit_percentage = request.POST.get('profit')
        breed = Product.objects.get(pk=breed_id)    # pylint: disable=no-member
        # purchase_price=breed.price
        sales = Sales(breed=breed,profit_percentage=profit_percentage)
        sales.save()
        messages.success(request,'Your Data Added successfully!')
        return redirect('sales')
    
def Del_Sales(request, id):
    try:
        dele = Sales.objects.get(id=id) # pylint: disable=no-member
        dele.delete()
        messages.success(request, 'Data successfully deleted!')
    except Sales.DoesNotExist:   # pylint: disable=no-member
        messages.error(request, 'Data not found or could not be deleted.')
    
    return redirect('sales')

def CheckOut(request):     # pylint: disable=no-member
    if request.method == 'POST':
       phone = request.POST.get('phone')
       address = request.POST.get('address')
       pincode = request.POST.get('pincode')
       order_status = request.POST.get('order_status')
       pro = request.POST.get('pid')
       product = Product.objects.get(pk=pro)       # pylint: disable=no-member
       payment_method = request.POST.get('payment_method')
       cart=request.session.get('cart')
       uid=request.session.get('_auth_user_id')
       user=User.objects.get(pk=uid)     # pylint: disable=no-member
       for i in cart:
           order=Order(
               user=user,
               name=cart[i]['name'],
               price=cart[i]['price'],
               quantity=cart[i]['quantity'],
               image=cart[i]['image'],
            #    product_id=cart[i]['product_id'],
               address=address,
               order_status=order_status,
               phone=phone,
               pincode=pincode,
               pid=product,
               payment_method=payment_method,
           )
           order.save()
           if payment_method=="Esewa":
               return redirect(f"/esewarequest/?o_id={order.id}")  # pylint: disable=no-member
           else:
               messages.success(request,'Your Order is successfully!')
               return render(request,'UserDashboard/add_to_cart.html')
           
def Update_Form(request,id):
    orderreq=Order.objects.get(id=id)        # pylint: disable=no-member
    return render(request,'AdminDash/orderupdate.html',{'orderreq':orderreq})  

def Update_Order(request, id):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        order_status = request.POST.get('order_status')
        pro = request.POST.get('pid')
        product = Product.objects.get(pk=pro)  # pylint: disable=no-member
        payment_method = request.POST.get('payment_method')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        
        # Check if a user with the provided ID exists
        try:
            user = User.objects.get(pk=uid)  # pylint: disable=no-member
        except User.DoesNotExist:
            # Handle the case where the user does not exist
            # You can implement your custom logic or redirect to a login page
            return redirect('login')  # Replace 'login' with your actual login URL

        # Check if an order with the provided ID exists
        try:
            order = Order.objects.get(pk=id)  # pylint: disable=no-member
        except Order.DoesNotExist:
            # Handle the case where the order does not exist
            # You can return an error page or redirect to a different view
            return redirect('error_page')  # Replace 'error_page' with your error page URL

        if cart:
            for i in cart:
                order.user = user
                order.name = cart[i]['name']
                order.price = cart[i]['price']
                order.quantity = cart[i]['quantity']
                order.image = cart[i]['image']
                order.address = address
                order.phone = phone
                order.order_status = order_status
                order.pincode = pincode
                order.pid = product
                order.payment_method = payment_method
                order.save()

            return redirect('orderinfo')
           
class Esewa_RequestView(View):
    def get(self, request, *args, **kwargs):
        o_id = request.GET.get("o_id")
        order = Order.objects.get(id=o_id)     # pylint: disable=no-member
        context = {
            "order": order
        }
        return render(request, "UserDashboard/esewarequest.html", context)
    
class EsewaVerifyView(View):
    def get(self, request, *args, **kwargs):
        # import xml.etree.ElementTree as ET
        oid = request.GET.get("oid")
        amt = request.GET.get("amt")
        refId = request.GET.get("refId")

        url = "https://uat.esewa.com.np/epay/transrec"
        d = {
            'amt': amt,
            'scd': 'epay_payment',
            'rid': refId,
            'pid': oid,
        }
        resp = requests.post(url, d)
        order_id = oid.split("_")[1]
        order_obj = Order.objects.get(id=order_id)                                       # pylint: disable=no-member
        print("status code=====",resp.status_code)
        if resp.status_code==200:
            order_obj.payment_completed = True
            order_obj.save()
            messages.success(request,'Your Payment is successful!')
            return render(request, "UserDashboard/esewarequest.html")
        else:
         return render(request,'/')
        
def Inventory(request):
    pr = Order.objects.all()                               # pylint: disable=no-member
    return render(request, 'AdminDash/Inventory.html', {'pr': pr})

def Order_Info(request):
    order = Order.objects.all()                               # pylint: disable=no-member
    return render(request, 'AdminDash/OrderList.html', {'order': order})

def Dashboard_View(request):
   result1 = Order.objects.values('name').annotate(max_quantity=Max('quantity')).order_by('-max_quantity')[:1] # pylint: disable=no-member
#    result2 = Order.objects.values('name').annotate(max_quantity=Max('quantity')).order_by('-min_quantity')[:1]
#    result3 = Product.objects.values('name').annotate(max_quantity=Max('profit')).order_by('profit')[:1]
   order=Order.objects.all()                               # pylint: disable=no-member

   quantities = Order.objects.values_list('quantity', flat=True)                          # pylint: disable=no-member
   return render(request, 'AdminDashboard.html', {'order':order,'quantities':quantities,'result1':result1,})
