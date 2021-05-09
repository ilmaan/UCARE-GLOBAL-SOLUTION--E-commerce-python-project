from django.shortcuts import render
from django.views import View
from .models import Customer, Cart, Product, OrderPlaced

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
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

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

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/module.html')
