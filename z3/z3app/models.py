from django.db import models
from django.db.models import CASCADE


# характеристики
class SpecGpu(models.Model):

    frequency_Mhz = models.IntegerField()
    memory_size_Gb = models.IntegerField()
    type_memory_str = models.CharField()


class Gpu(models.Model):

    name = models.CharField(max_length=30)
    price = models.FloatField()
    spec_id_foreign = models.OneToOneField(SpecGpu, on_delete=CASCADE, primary_key=True)


class Customer(models.Model):

    name = models.CharField(max_length=50)


class Purchase(models.Model):

    date_purshase = models.DateTimeField()
    amount_rub = models.IntegerField()
    gpu_id_foreign = models.ForeignKey(Gpu, on_delete=CASCADE)
    customer_id_foreign = models.ForeignKey(Customer, on_delete=CASCADE)




