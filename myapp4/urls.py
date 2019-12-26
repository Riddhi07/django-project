from django.contrib import admin
from django.urls import path
from . import views
urlpatterns =[
    path('',views.Homepage),
    path('Compair/',views.Compair,name='compair'),
    path('Components/',views.Components,name='components'),
    path('Contact/',views.Contact,name='contact'),
    path('Faq/',views.Faq,name='faq'),
    path('Forgetpass/',views.Forgetpass,name='forgetpass'),
    path('Index/',views.Index,name='index'),
    path('Legal_notice/',views.Legal_notice,name='legal_notice'),
    path('Login/',views.Login,name='login'),
    path('Normal/',views.Normal,name='normal'),
    path('Productdetails/',views.Productdetails,name='product_details'),
    path('Productsummary/',views.Productsummary,name='product_summary'),
    path('Products/',views.Products,name='products'),
    path('Register/',views.Register,name='register'),
    path('Special_offer/',views.Special_offer,name='special_offer'),
    path('Tac/',views.Tac,name='tac'),
]
