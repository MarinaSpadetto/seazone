from django.db import models
import uuid
from advertisement.models import Advertisement


class Reservation(models.Model):
    cod_reservation = models.UUIDField(default=uuid.uuid4, editable=False)
    advertisement = models.ForeignKey(Advertisement, models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.CharField(max_length=255)
    number_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}'
