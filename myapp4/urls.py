from django.contrib import admin
from django.urls import path
from . import views
urlpatterns =[
    path('',views.Index),   
    path('loginpage/',views.loginpage,name='login'),

    path('field/',views.fieldpage,name='field'),
    path('delfd/<int:id>',views.delfd),
    path('editfd/<int:id>',views.editfd),
    path('editfd/upfd/<int:id>', views.upfd),


    path('Category/',views.categorypage,name='category'),
    path('delcat/<int:id>',views.delcn),
    path('editcat/<int:id>', views.editcat),
    path('upcat/<int:id>', views.upcat),


    path('Delievery/',views.delieverypage,name='delievery'),
    path('deldl/<int:id>',views.deldl),
    path('editdl/<int:id>', views.editdl),
    path('updl/<int:id>', views.updl),


    path('Variant/',views.variantpage,name='variant'),
    path('delvt/<int:id>',views.delvt),
    path('editvt/<int:id>', views.editvt),
    path('upvt/<int:id>', views.upvt),


    path('Option/',views.optionpage,name='option'),
    path('delop/<int:id>',views.delop),
    path('editop/<int:id>', views.editop),
    path('upop/<int:id>', views.upop),


    path('Material/',views.materialpage,name='material'),
    path('delmt/<int:id>',views.delmt),
    path('editmt/<int:id>', views.editmt),
    path('upmt/<int:id>', views.upmt),


    path('Product/',views.productpage,name='product'),
    path('delpd/<int:id>',views.delpd),
    path('editpd/<int:id>', views.editpd),
    path('uppd/<int:id>', views.uppd),


    path('Image/',views.imagepage,name='image'),
    path('delim/<int:id>',views.delim),
    path('editim/<int:id>', views.editim),
    path('upim/<int:id>', views.upim),


    path('Payment/',views.paymentpage,name='payment'),



    path('Customer/',views.customerpage,name='customer'),
    path('Order/',views.orderpage,name='order'),
    path('Contact/',views.contactpage,name='contact'),
    path('Contact/',views.contactpage,name='contact'),

]
