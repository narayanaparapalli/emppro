from django import forms
from product_app.models import Product,Reg

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


# class UpdateForm(forms.Form):
#     pid =forms.IntegerField(label='enter pid',max_length=20)
#     pcost=forms.DecimalField(label='enter pcost',max_length=20)

class UpdateForm(forms.Form):
    pid=forms.CharField(label='Enter pid',max_length=20)
    pcost=forms.CharField(label='Enter pcost',max_length=20)


class DeleteForm(forms.Form):
    pid=forms.IntegerField()

class RegForm(forms.Form):
    fname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter First Name',

            }
        )
    )
    lname=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Last Name',
            }
        )
    )
    user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter User Name',
            }
        )
    )
    pwd = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'*******',
            }
        )
    )
    mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'siva@gmail.com',
            }
        )
    )
    dob=forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'yyyy/mm/d '
            }
        )
    )
    gender=forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form control',
                'place holder':'Gender',
            }
        )
    )

class LoginForm(forms.Form):
    user =forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )
    pwd = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        )
    )


