from django.db import models
from property.models import Property


class Advertisement(models.Model):

    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=255)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.property.cod_property}'
