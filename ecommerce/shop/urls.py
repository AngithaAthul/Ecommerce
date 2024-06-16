from django.urls import path
from django.contrib import admin
from . import views
 
 # Django admin header customization
admin.site.site_header="ORGANIC"
admin.site.site_title="Welcome to ORGANIC STORE Dashboard"
admin.site.index_title="Welcome to this Portal "
urlpatterns= [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('cart/',views.cart_page,name="cart"),
    path('fav/',views.fav_page,name="fav"),
    path('favviewpage/',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('collections/',views.collections,name="collections"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart/',views.add_to_cart,name="addtocart"),
]