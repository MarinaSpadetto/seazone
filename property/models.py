from django.db import models


class Property(models.Model):
    cod_property = models.CharField(max_length=6, unique=True)
    limit_guests = models.IntegerField()
    quantity_bathroom = models.IntegerField()
    allowed_pets = models.BooleanField()
    cleaning_fee = models.DecimalField(max_digits=10, decimal_places=2)
    activation_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cod_property
