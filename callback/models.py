from django.core.validators import MinValueValidator
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Company(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Billing(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )
    services = models.ManyToManyField(Service)
    account = models.PositiveIntegerField(
        validators=[
            MinValueValidator(
                limit_value=1,
                message='The account number cannot be less than 1'
            )
        ]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
