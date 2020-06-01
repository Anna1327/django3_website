from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .settings.base import *

# Create your views here.


class IndexView(View):

    def get(self, request):
        return render(request, 'myproj/index.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                     'shop_name': SHOP_NAME,  'address': ADDRESS})


class BlogView(View):

    def get(self, request):
        return render(request, 'myproj/blog.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                     'shop_name': SHOP_NAME,  'address': ADDRESS})


class BlogDetailsView(View):

    def get(self, request):
        return render(request, 'myproj/blog-details.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                            'shop_name': SHOP_NAME,  'address': ADDRESS})


class CheckOutView(View):

    def get(self, request):
        return render(request, 'myproj/check-out.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                         'shop_name': SHOP_NAME,  'address': ADDRESS})


class ContactView(View):

    def get(self, request):
        return render(request, 'myproj/contact.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                       'shop_name': SHOP_NAME,  'address': ADDRESS})


class FaqView(View):

    def get(self, request):
        return render(request, 'myproj/faq.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                   'shop_name': SHOP_NAME,  'address': ADDRESS})


class LoginView(View):

    def get(self, request):
        return render(request, 'myproj/login.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                     'shop_name': SHOP_NAME,  'address': ADDRESS})

    def post(self, request):
        html = '<html><body>'
        for key, value in request.POST.items():
            html += f'{key}: {value}<br>'
            print(key, value)
        html += '</body></html>'
        return HttpResponse(html)


class ProductView(View):

    def get(self, request):
        return render(request, 'myproj/product.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                       'shop_name': SHOP_NAME,  'address': ADDRESS})


class RegisterView(View):

    def get(self, request):
        return render(request, 'myproj/register.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                        'shop_name': SHOP_NAME,  'address': ADDRESS})


class ShopView(View):

    def get(self, request):
        return render(request, 'myproj/shop.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                    'shop_name': SHOP_NAME,  'address': ADDRESS})


class ShoppingCartView(View):

    def get(self, request):
        return render(request, 'myproj/shopping-cart.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                             'shop_name': SHOP_NAME,  'address': ADDRESS})