from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseNotFound
from .settings.base import *
from .forms import ProductForm
from .models import *

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


class ProductCreateView(View):

    def get(self, request):
        form = ProductForm()
        return render(request, 'myproj/create-product.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                              'shop_name': SHOP_NAME,  'address': ADDRESS,
                                                              'form': form})

    def post(self, request):
        if request.method == 'POST':
            bound_form = ProductForm(request.POST, request.FILES)
            if bound_form.is_valid() and not None:
                if bound_form['name'] and bound_form['brand'] and bound_form['color'] and bound_form['size'] \
                        and bound_form['tags'] and bound_form['price'] not in ProductForm():
                    bound_form.save()
                    func_st = 'Product created successfully!'
                else:
                    func_st = 'Such product already exists!'

                return render(request, 'myproj/done.html', {'func_st': func_st})
            else:
                return render(request, 'myproj/create-product.html', {'form': bound_form})


class ProductUpdate(View):

    def get(self, request):
        product = Products.objects.all()

        return render(request, 'myproj/update.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                      'shop_name': SHOP_NAME, 'address': ADDRESS,
                                                      'product': product})


def delete(request, id):
    try:
        product = Products.objects.get(id=id)
        product.delete()
        func_st = 'Product deleted successfully!'
        return render(request, 'myproj/done.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                    'shop_name': SHOP_NAME, 'address': ADDRESS,
                                                    'func_st': func_st})
    except Products.DoesNotExist:
        return HttpResponseNotFound("<h2>Sorry, Product not found</h2>")


def edit(request, id):
    try:
        product = Products.objects.get(id=id)
        form = ProductForm()

        if request.method == "POST":
            product.category = request.POST.get("category")
            product.name = request.POST.get("name")
            product.image = request.POST.get("image")
            product.color = request.POST.get("color")
            product.brand = request.POST.get("brand")
            product.size = request.POST.get("size")
            product.tags = request.POST.get("tags")
            product.price = request.POST.get("price")
            product.price_sale = request.POST.get("price_sale")
            product.save()
            func_st = 'Product updated successfully!'
            return render(request, 'myproj/done.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                        'shop_name': SHOP_NAME, 'address': ADDRESS,
                                                        'func_st': func_st})

        return render(request, 'myproj/edit-product.html', {'phone_number': PHONE_NUMBER, 'email': EMAIL,
                                                            'shop_name': SHOP_NAME, 'address': ADDRESS,
                                                            'product': product, 'form': form})
    except Products.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

