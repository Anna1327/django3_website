from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', IndexView.as_view()),
    path('index/', IndexView.as_view(), name='index'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog-details/', BlogDetailsView.as_view(), name='blog-details'),
    path('check-out/', CheckOutView.as_view(), name='check-out'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('login/', LoginView.as_view(), name='login'),
    path('product/', ProductView.as_view(), name='product'),
    path('register/', RegisterView.as_view(), name='register'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shopping-cart/', ShoppingCartView.as_view(), name='shopping-cart'),
    path('create/', ProductCreateView.as_view(), name='create-product'),
    path('delete/<int:id>/', views.delete, name='delete-id'),
    path('update/', ProductUpdate.as_view(),  name='update'),
    path('edit/<int:id>/', views.edit, name='edit-id'),

]
