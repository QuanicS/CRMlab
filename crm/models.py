from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    address = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    cost = models.FloatField(null=True)
    vendor = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=300, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete= models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=(
        ('ОТМЕНЕНО','ОТМЕНЕНО'),
        ('ЗАВЕРШЁН','ЗАВЕРШЁН'),
        ('ВОЗВРАТ','ВОЗВРАТ'),
        ('ОЖИДАНИЕ ОПЛАТЫ','ОЖИДАНИЕ ОПЛАТЫ'),
    ))

