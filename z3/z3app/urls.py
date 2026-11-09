



from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("customers/", views.customers, name="customers"),
    path("products/", views.products, name="products"),
    path("sales_prodress/", views.sales_progress, name="sales_progress"),
    path("sale/", views.sale, name="sale"),
]