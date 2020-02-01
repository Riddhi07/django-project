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
            'dtype':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'catname'})
            }

class variantform(forms.ModelForm):
    class Meta:
        model=Variant
        fields='__all__'
        widgets={
            'label':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'label'}),
            'value':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'value'})
            }

class optionform(forms.ModelForm):
    class Meta:
        model=Option
        fields='__all__'
        widgets={
            'label':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'label'}),
            'value':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'value'})
            }

class materialform(forms.ModelForm):
    class Meta:
        model=Material
        fields='__all__'
        widgets={
            'label':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'label'}),
            'value':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'value'})
            }
class productform(forms.ModelForm):
    class Meta:
         model=Product
         fields='__all__'
         widgets={
             'catid':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'catid'}),
             'heading':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'heading'}),
             'subheading':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'subheading'}),
             'highlight':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'highlight'}),

             'companyname':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'companyname'}),
             'ptype':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'type'}),
             'brand':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'brand'}),
             'optionid':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'optionid'}),
             'mid':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'mid'}),
             'versionid':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'versionid'}),

             'modelno':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'modelno'})
             }

class imageform(forms.ModelForm):
    class Meta:
        model=Image
        fields='__all__'
        widgets={
            'image1':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'image1'}),
            'image2':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'image2'}),
            'image3':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'image3'}),
            'image4':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'image4'}),
            'image5':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'image5'}),
            'image6':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'image6'}),
            'image7':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'image7'}),
            'itemid':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'itemid'})
            }

class paymethodform(forms.ModelForm):
    class Meta:
        model=Paymethod
        fields='__all__'
        widgets={
            'pmname':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'pmname'}),
            'pvalue':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'pvalue'})
            }

# class customerform(forms.ModelForm):
#     class Meta:
#         model=Customer
#         fields='__all__'
#         widgets={
#             'emailid':forms.EmailInput(),
#             'contact1':forms.IntegerField(),
#             'contact2':forms.IntegerField(),
#             'address':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'address'}),
#             'pincode':forms.IntegerField(),
#             'cname':forms.TextInput(attrs={'çlass':'input-xlarge','placeholder':'cname'})
#             }

# class orderform(forms.ModelForm):
#     class Meta:
#         model=Order
#         fields='__all__'
#         widgets={
#             'itemid':forms.IntegerField()
#             }

class contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'conname':forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Name'}),
            'emailid':forms.EmailInput(),
            'subject':forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Subject'}),
            'desc':forms.Textarea(attrs={'class':'input-xlarge','placeholder':'desc'})
            }

