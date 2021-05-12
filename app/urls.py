from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('printer/', views.printer, name='printer'),
    path('printer/<slug:data>', views.printer, name='printerdata'),
    path('camera/', views.camera, name='camera'),
    path('camera/<slug:data>', views.camera, name='cameradata'),
    path('computer/', views.computer, name='computer'),
    path('computer/<slug:data>', views.computer, name='computerdata'),
    path('antivirus/', views.antivirus, name='antivirus'),
    path('antivirus/<slug:data>', views.antivirus, name='antivirusdata'),
    path('login/', views.login, name='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
