from django.db import models
from advertisement.models import Advertisement


class Reservation(models.Model):
    cod_reservation = models.CharField(max_length=6, unique=True)
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

    def save(self, *args, **kwargs):
        if not self.cod_reservation:
            last_reservation = Reservation.objects.order_by(
                '-cod_reservation').first()
            if last_reservation:
                last_number = int(last_reservation.cod_reservation[3:])
                new_number = last_number + 1
            else:
                new_number = 1
            self.cod_reservation = f'PRT{str(new_number).zfill(3)}'
        super(Reservation, self).save(*args, **kwargs)
