from django.urls import path
from productsapp import views as productsapp
from productsapp.views import ProductsView

app_name = 'productsapp'

urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('<slug:slug>', productsapp.product, name='product'),
    path('product/<slug:slug>', productsapp.product_update, name='product_update'),
    path('product/service/update/<slug:slug>', productsapp.product_service_update, name='product_service_update'),
    path('product/work/update/<slug:slug>', productsapp.product_work_update, name='product_work_update')
]
