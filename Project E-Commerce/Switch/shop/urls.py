from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="shopIndex"),
    path('product/', views.product, name="productPage"),
    path('productView/<int:id>', views.prodView, name="productDetailPage"),
    path('search/', views.search, name="search"),
    path('about/', views.about, name="aboutUs"),
    path('contact/', views.contact, name="contactUs"),
    path('checkOut/', views.checkOut, name="checkOut"),
]
