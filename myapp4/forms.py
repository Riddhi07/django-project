from django import forms
from .models import Field,Category,Delievery,Variant,Material,Option,Image,Order,Product,Paymethod,Customer,Contact

class fieldform(forms.ModelForm):
    class Meta:
        model=Field
        fields='__all__'
        widgets={
            'fname':forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Name'})
            }

class categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        widgets={
            'pid':forms.Select(choices=Field.objects.values_list('id','fname'),attrs={'class': 'input-xlarge', 'placeholder': 'pid'}),
            'catname': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'catname'})
            }

class delieveryform(forms.ModelForm):
    class Meta:
        model=Delievery
        fields='__all__'
        widgets={
            'dtype':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'catname'))
            }

class variantform(forms.ModelForm):
    class Meta:
        model=Variant
        fields='__all__'
        widgets={
            'label':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'label')),
            'value':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'value'))
            }

class optionform(forms.ModelForm):
    class Meta:
        model=Option
        fields='__all__'
        widgets={
            'label':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'label')),
            'value':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'value'))
            }

class materialform(forms.ModelForm):
    class Meta:
        model=Material
        fields='__all__'
        widgets={
            'label':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'label')),
            'value':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'value'))
            }


class productform(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        widgets={
            # add a foreignkey field catid here
            'heading':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'heading')),
            'subheading':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'subheading')),
            'actualprice':forms.IntegerField(attrs=('çlass':'input-xlarge','placeholder':'actualprice')),
            'discount':forms.IntegerField(attrs=('çlass':'input-xlarge','placeholder':'discount')),
            'highlight':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'highlight')),
            'description':forms.FilePathField(attrs=('çlass':'input-xlarge','placeholder':'highlight')),
            'companyname':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'companyname')),
            'type':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'type')),
            'brand':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'brand')),
            'companyname':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'companyname')),
            # add a foreignkey field optionid here
            # add a foreignkey field mid here
            # add a foreignkey field versionid here
            'availability':forms.BooleanField(attrs=('class':'input-xlarge','placeholder':'availability')),
            'modelno':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'modelno'))
            }

class imageform(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
        widgets={
            'image1':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'image1')),
            'image2':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'image2')),
            'image3':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'image3')),
            'image4':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'image4')),
            'image5':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'image5')),
            'image6':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'image6')),
            'image7':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'image7'))
            # add a foreign key field itemid here
            }

class paymethodform(forms.ModelForm):
    class Meta:
        model=Paymethod
        fields='__all__'
        widgets={
            'pmname':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'pmname')),
            'pvalue':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'pvalue'))
            }

class customerform(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        widgets={
            'emailid':forms.EmailField(attrs=('çlass':'input-xlarge','placeholder':'emailid')),
            'contact1':forms.IntegerField(attrs=('çlass':'input-xlarge','placeholder':'contact1')),
            'contact2':forms.IntegerField(attrs=('çlass':'input-xlarge','placeholder':'contact2')),
            'address':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'address')),
            'pincode':forms.IntegerField(attrs=('çlass':'input-xlarge','placeholder':'pincode')),
            'cname':forms.TextInput(attrs=('çlass':'input-xlarge','placeholder':'cname'))
            }

class orderform(forms.ModelForm):
    class Meta:
        model=Order
        fields='__all__'
        widgets={
            'itemid':forms.IntegerField(attrs=('çlass':'input-xlarge','placeholder':'itemid'))
            }

class contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'conname':forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Name'}),
            'emailid':forms.EmailInput(attrs={'class':'input-xlarge','placeholder':'Email'}),
            'subject':forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Subject'}),
            'desc':forms.Textarea(attrs={'class':'input-xlarge','placeholder':''})
        }


