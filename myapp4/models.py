from django.db import models

# Create your models here.
class Field(models.Model):
    fname=models.CharField(max_length=100)

class Category(models.Model):
    pid=models.IntegerField()
    catname=models.CharField(max_length=100)

class Delievery(models.Model):
    dtype=models.CharField(max_length=100)

class Variant(models.Model):
    label=models.CharField(max_length=100)
    value=models.CharField(max_length=100)

class Option(models.Model):
    label=models.CharField(max_length=100)
    value=models.CharField(max_length=100)

class Material(models.Model):
    label=models.CharField(max_length=100)
    value=models.CharField(max_length=100)

class Product(models.Model):
    catid=models.CharField(max_length=100)
    heading=models.CharField(max_length=100)
    subheading=models.CharField(max_length=100)
    actualprice=models.FloatField()
    discount=models.FloatField()
    highlight=models.TextField(max_length=500)
    description=models.FilePathField()
    companyname=models.CharField(max_length=200)
    ptype=models.CharField(max_length=200)
    brand=models.CharField(max_length=50)
    optionid=models.CharField(max_length=100)
    mid=models.CharField(max_length=100)
    versionid=models.CharField(max_length=100)
    availability=models.BooleanField()
    modelno=models.CharField(max_length=100)

class Image(models.Model):
    image1=models.CharField(max_length=200)
    image2=models.CharField(max_length=200)
    image3=models.CharField(max_length=200)
    image4=models.CharField(max_length=200)
    image5=models.CharField(max_length=200)
    image6=models.CharField(max_length=200)
    image7=models.CharField(max_length=200)
    itemid=models.CharField(max_length=100)


class Paymethod(models.Model):
    pmname=models.CharField(max_length=100)
    pvalue=models.CharField(max_length=100)

class Customer(models.Model):
    emailid=models.EmailField(max_length=100)
    contact1=models.IntegerField()
    contact2=models.IntegerField()
    address=models.CharField(max_length=100)
    pincode=models.IntegerField()
    cname=models.CharField(max_length=100)

class Order(models.Model):
    itemid=models.IntegerField()

class Contact(models.Model):
    conname=models.CharField(max_length=100)
    emailid = models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    desc=models.CharField(max_length=255)

