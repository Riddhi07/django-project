from django.shortcuts import render,redirect
from .models import Contact,Field,Paymethod,Product,Category,Delievery,Variant,Option
from .forms import contactform,categoryform,fieldform,delieveryform,variantform,optionform
from django.http import HttpResponse
"""
def Compair(request):
    return render(request,'compair.html')

def Homepage(request):
    a=['Hello']
    return HttpResponse("<h1>Hey there!</h1>".format(a))

def Components(request):
    return render(request,'components.html')

def Contact(request):
    form=contactform()
    form1=categoryform()
    return render(request,'contact.html',{'form':form,'form1':form1})
def Faq(request):
    return render(request,'faq.html')

def Forgetpass(request):
    return render(request,'forgetpass.html')



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

def category(request):
    return render(request,'category.html')

def dashpage(request):
    return render(request,'dashboard-2.html')

def loginpage(request):
    return render(request,'loginad.html')

def registerpage(request):
    return render(request,'registerad.html')

def formpage(request):
    return render(request,'form.html')


def contactad(request):
    return render(request,'contactad.html')

def statictable(request):
    return render(request,'static-table.html')

"""
def Index(request):
    return render(request,'index.html')
def loginpage(request):
    return render(request,'loginad.html')


def fieldpage(request):
    if request.method=='POST':
        f=fieldform(request.POST)
        if f.is_valid():
            try:
                f.save()
                #return redirect('field.html')
            except:
                pass
    else:
        f=fieldform()
        fshow=Field.objects.all()
        return render(request,'field.html',{'f':f,'fshow':fshow})
    f=fieldform()
    fshow=Field.objects.all()
    return render(request,'field.html',{'f':f,'fshow':fshow})
def delfd(request,id):
    dfd=Field.objects.get(id=id)
    dfd.delete()
    return redirect('/field')
def editfd(request,id):
    if request.method == "POST":
        efd = Field.objects.get(id=id)
        form = fieldform(request.POST, instance=efd)
        if form.is_valid():
            try:
                form.save()
                return redirect('field')
            except:
                pass
    else:
        efd = Field.objects.get(id=id)
        fshow = Field.objects.all()
        return render(request,'editfd.html',{'efd':efd,'fshow': fshow})
def upfd(request,id):
    efd = Field.objects.get(id=id)
    form = fieldform(request.POST,instance=efd)
    if form.is_valid():
        try:
            form.save()
            return redirect('field')
        except:
            pass
    return render(request, 'editfd.html', {'efd': efd})


def categorypage(request):
    if request.method=='POST':
        f=categoryform(request.POST)
        if f.is_valid():
            try:
                f.save()
                #return redirect('field.html')
            except:
                pass
    else:
        f=fieldform()
        fshow=Category.objects.all()
        return render(request,'category1.html',{'f':f,'fshow':fshow})
    f=categoryform()
    fshow=Category.objects.all()
    return render(request,'category1.html',{'f':f,'fshow':fshow})
def delcn(request,id):
    dcn=Category.objects.get(id=id)
    dcn.delete()
    return redirect('/Category')
def editcat(request,id):
    if request.method == "POST":
        ecat = Category.objects.get(id=id)
        form = categoryform(request.POST, instance=ecat)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Category')
            except:
                pass
    else:
        ecat = Category.objects.get(id=id)
        fshow = Category.objects.all()
        return render(request,'editcat.html',{'ecat':ecat,'fshow': fshow})
def upcat(request,id):
    efd = Category.objects.get(id=id)
    form = categoryform(request.POST,instance=efd)
    if form.is_valid():
        try:
            form.save()
            return redirect('category')
        except:
            pass
    return render(request, 'editcat.html', {'ecat': efd})


def delieverypage(request):
    if request.method=='POST':
        f=delieveryform(request.POST)
        if f.is_valid():
            try:
                f.save()
                #return redirect('field.html')
            except:
                pass
    else:
        f=delieveryform()
        fshow=Delievery.objects.all()
        return render(request,'delievery.html',{'f':f,'fshow':fshow})
    f=delieveryform()
    fshow=Delievery.objects.all()
    return render(request,'delievery.html',{'f':f,'fshow':fshow})
def deldl(request,id):
    dcn=Delievery.objects.get(id=id)
    dcn.delete()
    return redirect('/Delievery')
def editdl(request,id):
    if request.method == "POST":
        edl = Delievery.objects.get(id=id)
        form = delieveryform(request.POST, instance=edl)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Delievery')
            except:
                pass
    else:
        edl = Delievery.objects.get(id=id)
        fshow = Delievery.objects.all()
        return render(request,'editdl.html',{'edl':edl,'fshow': fshow})
def updl(request,id):
    efd = Delievery.objects.get(id=id)
    form = delieveryform(request.POST,instance=efd)
    if form.is_valid():
        try:
            form.save()
            return redirect('delievery')
        except:
            pass
    return render(request, 'editdl.html', {'edl': efd})


def variantpage(request):
    if request.method=='POST':
        f=variantform(request.POST)
        if f.is_valid():
            try:
                f.save()
                #return redirect('field.html')
            except:
                pass
    else:
        f=variantform()
        fshow=Variant.objects.all()
        return render(request,'variant.html',{'f':f,'fshow':fshow})
    f=variantform()
    fshow=Variant.objects.all()
    return render(request,'variant.html',{'f':f,'fshow':fshow})
def delvt(request,id):
    dcn=Variant.objects.get(id=id)
    dcn.delete()
    return redirect('/Variant')
def editvt(request,id):
    if request.method == "POST":
        edl = Variant.objects.get(id=id)
        form = variantform(request.POST, instance=edl)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Variant')
            except:
                pass
    else:
        edl = Variant.objects.get(id=id)
        fshow = Variant.objects.all()
        return render(request,'editvt.html',{'edl':edl,'fshow': fshow})
def upvt(request,id):
    efd = Variant.objects.get(id=id)
    form = variantform(request.POST,instance=efd)
    if form.is_valid():
        try:
            form.save()
            return redirect('variant')
        except:
            pass
    return render(request, 'editvt.html', {'edl': efd})


def optionpage(request):
    if request.method=='POST':
        f=optionform(request.POST)
        if f.is_valid():
            try:
                f.save()
                #return redirect('field.html')
            except:
                pass
    else:
        f=optionform()
        fshow=Option.objects.all()
        return render(request,'option.html',{'f':f,'fshow':fshow})
    f=optionform()
    fshow=Option.objects.all()
    return render(request,'variant.html',{'f':f,'fshow':fshow})
def delop(request,id):
    dcn=Option.objects.get(id=id)
    dcn.delete()
    return redirect('/Option')
def editop(request,id):
    if request.method == "POST":
        edl = Option.objects.get(id=id)
        form = optionform(request.POST, instance=edl)
        if form.is_valid():
            try:
                form.save()
                return redirect('/Option')
            except:
                pass
    else:
        edl = Option.objects.get(id=id)
        fshow = Option.objects.all()
        return render(request,'editop.html',{'edl':edl,'fshow': fshow})
def upop(request,id):
    efd = Option.objects.get(id=id)
    form = optionform(request.POST,instance=efd)
    if form.is_valid():
        try:
            form.save()
            return redirect('option')
        except:
            pass
    return render(request, 'editop.html', {'edl': efd})


def materialpage(request):
    return render(request,'material.html')
def productpage(request):
    return render(request,'product.html')
def imagepage(request):
    return render(request,'image.html')
def paymentpage(request):
    return render(request,'payment.html')
def customerpage(request):
    return render(request,'customer.html')
def orderpage(request):
    return render(request,'order1.html')
def contactpage(request):
    return render(request,'contact.html')
