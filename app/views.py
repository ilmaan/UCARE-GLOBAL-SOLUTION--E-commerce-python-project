from django.contrib.auth import load_backend
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Customer, Cart, Product, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        laptop = Product.objects.filter(category='LP')
        computer = Product.objects.filter(category='CR')
        printer = Product.objects.filter(category='PR')
        camera = Product.objects.filter(category='CA')
        antivirus = Product.objects.filter(category='AV')
        network_firewall = Product.objects.filter(category='NF')
        return render(request,'app/home.html',{'laptop':laptop,'computer':computer,'printer':printer,'camera':camera,'antivirus':antivirus,'network_firewall':network_firewall})
        

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,Product=product).save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        # print(cart)
        amount = 0.0
        shipping = 15.00
        total_amount = 0.00
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.Product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping
            return render(request, 'app/addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount})
        else:
            return render(request,'app/home.html')

def pluscart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        c = Cart.objects.get(Q(Product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping = 15.00
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.Product.discounted_price)
            amount += tempamount
            totalamount = amount + shipping


        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
            }
        return JsonResponse(data)


def buy_now(request):
     return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primry'})

def orders(request):
 return render(request, 'app/orders.html')

# def change_password(request):
#  return render(request, 'app/changepassword.html')

def laptop(request,data=None):
    if data == None:
        laptop = Product.objects.filter(category='LP')
    elif data =='below':
        laptop = Product.objects.filter(category='LP').filter(discounted_price__lt=301)
    elif data =='above':
        laptop = Product.objects.filter(category='LP').filter(discounted_price__lt=401) 
    elif data =='highest':
        laptop = Product.objects.filter(category='LP').filter(discounted_price__gt=401)       

    return render(request, 'app/laptop.html',{'laptop':laptop})

def computer(request,data=None):
    if data == None:
        computer = Product.objects.filter(category='CR')
    elif data =='below':
        computer = Product.objects.filter(category='CR').filter(discounted_price__lt=701)
    elif data =='above':
        computer = Product.objects.filter(category='CR').filter(discounted_price__lt=1101) 
    elif data =='highest':
        computer = Product.objects.filter(category='CR').filter(discounted_price__gt=1101)       

    return render(request, 'app/computer.html',{'computer':computer})

def printer(request,data=None):
    if data == None:
        printer = Product.objects.filter(category='PR')
    elif data =='below':
        printer = Product.objects.filter(category='PR').filter(discounted_price__lt=701)
    elif data =='above':
        printer = Product.objects.filter(category='PR').filter(discounted_price__lt=1101) 
    elif data =='highest':
        printer = Product.objects.filter(category='PR').filter(discounted_price__gt=1101)       

    return render(request, 'app/printer.html',{'printer':printer})

def antivirus(request,data=None):
    if data == None:
        antivirus = Product.objects.filter(category='AV')
    elif data =='below':
        antivirus = Product.objects.filter(category='AV').filter(discounted_price__lt=701)
    elif data =='above':
        antivirus = Product.objects.filter(category='AV').filter(discounted_price__lt=1101) 
    elif data =='highest':
        antivirus = Product.objects.filter(category='AV').filter(discounted_price__gt=1101)       

    return render(request, 'app/antivirus.html',{'antivirus':antivirus})

def camera(request,data=None):
    if data == None:
        camera = Product.objects.filter(category='CA')
    elif data =='below':
        camera = Product.objects.filter(category='CA').filter(discounted_price__lt=121)
    elif data =='above':
        camera = Product.objects.filter(category='CA').filter(discounted_price__lt=160) 
    elif data =='highest':
        camera = Product.objects.filter(category='CA').filter(discounted_price__gt=171)       

    return render(request, 'app/camera.html',{'camera':camera})





# def login(request):
#  return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'You Have Successfully Registered')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})    



def checkout(request):
 return render(request, 'app/module.html')


class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Profile Updated Successfully')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})


        