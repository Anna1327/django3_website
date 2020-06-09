from django import forms
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile


class ProductForm(forms.Form):
    category = forms.CharField(max_length=50)
    name = forms.CharField(max_length=200)
    image = forms.ImageField()
    color = forms.CharField(max_length=20)
    brand = forms.CharField(max_length=30)
    size = forms.CharField(max_length=5)
    tags = forms.CharField(max_length=50)
    price = forms.CharField(max_length=10)
    price_sale = forms.CharField(max_length=10)

    category.widget.attrs.update({'class': 'form-control'})
    name.widget.attrs.update({'class': 'form-control'})
    image.widget.attrs.update({'c lass': 'form-control'})
    color.widget.attrs.update({'class': 'form-control'})
    brand.widget.attrs.update({'class': 'form-control'})
    size.widget.attrs.update({'class': 'form-control'})
    tags.widget.attrs.update({'class': 'form-control'})
    price.widget.attrs.update({'class': 'form-control'})
    price_sale.widget.attrs.update({'class': 'form-control'})

    def save(self):
        new_data = Products.objects.create(category=self.cleaned_data['category'],
                                           name=self.cleaned_data['name'],
                                           image=self.cleaned_data['image'],
                                           color=self.cleaned_data['color'],
                                           brand=self.cleaned_data['brand'],
                                           size=self.cleaned_data['size'],
                                           tags=self.cleaned_data['tags'],
                                           price=self.cleaned_data['price'],
                                           price_sale=self.cleaned_data['price_sale'])

        return new_data


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    confirm_password = forms.CharField(max_length=50)

    username.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    confirm_password.widget.attrs.update({'class': 'form-control'})

    def save(self):
        new_user = Register.objects.create(username=self.cleaned_data['username'],
                                           email=self.cleaned_data['email'],
                                           password=self.cleaned_data['password'],
                                           confirm_password=self.cleaned_data['confirm_password'])
        return new_user