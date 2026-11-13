



from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("customers/", views.customers, name="customers"),
    path("products/", views.products, name="products"),
    path("sales_progress/", views.sales_progress, name="sales_progress"),
    path("sale/", views.sale, name="sale"),

    path("create_client/", views.create_client, name='create_client'),
    path("edit_gpu/<int:id>", views.edit_gpu, name="edit_gpu"),
    path("create_gpu/", views.create_gpu, name="create_gpu"),

    path("edit_customer/<int:id>", views.edit_customer, name='edit_customer'),
    path("delete_customer/<int:id>", views.delete_customer, name='delete_customer'),
    path("success_buy/<int:id>", views.success_buy, name="success_buy"),
    path("delete_gpu/<int:id>", views.delete_gpu, name="delete_gpu"),
]