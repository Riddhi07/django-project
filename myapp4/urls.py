from django.contrib import admin
from django.urls import path
from . import views
urlpatterns =[
    path('',views.Index),   
    path('loginpage/',views.loginpage,name='login'),
    path('delfd/<int:id>',views.delfd),
    path('editfd/<int:id>',views.editfd),
    path('editfd/upfd/<int:id>', views.upfd),
    path('field/',views.fieldpage,name='field'),
    path('Contact/',views.contactpage,name='contact'),
    path('Category/',views.categorypage,name='category'),
    path('delcat/<int:id>',views.delcn),
    path('editcat/<int:id>', views.editcat),
    path('upcat/<int:id>', views.upcat),
    path('Delievery/',views.delieverypage,name='delievery'),
    path('Category/',views.Contact,name='category'),
    path('Variant/',views.variantpage,name='variant'),
    path('Option/',views.optionpage,name='option'),
    path('Material/',views.materialpage,name='material'),
    path('Product/',views.productpage,name='product'),
    path('Image/',views.imagepage,name='image'),
    path('Payment/',views.paymentpage,name='payment'),
    path('Customer/',views.customerpage,name='customer'),
    path('Order/',views.orderpage,name='order'),
    path('Contact/',views.contactpage,name='contact'),

]
