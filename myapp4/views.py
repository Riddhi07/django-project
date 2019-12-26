from django.shortcuts import render
from django.http import HttpResponse
def Homepage(request):
    a=['Hello']
    return HttpResponse("<h1>Hey there!</h1>".format(a))
def Compair(request):
    return render(request,'compair.html')

def Components(request):
    return render(request,'components.html')

def Contact(request):
    return render(request,'contact.html')

def Faq(request):
    return render(request,'faq.html')

def Forgetpass(request):
    return render(request,'forgetpass.html')

def Index(request):
    return render(request,'index.html')

def Legal_notice(request):
    return render(request,'legal_notice.html')

def Login(request):
    return render(request,'login.html')

def Masterfront(request):
    return render(request,'master-front.html')

def Normal(request):
    return render(request,'normal.html')

def Productdetails(request):
    return render(request,'products.html')

def Productsummary(request):
    return render(request,'product_summary.html')

def Products(request):
    return render(request,'products.html')

def Register(request):
    return render(request,'register.html')

def Special_offer(request):
    return render(request,'special_offer.html')

def Tac(request):
    return render(request,'tac.html')


