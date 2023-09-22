from django.contrib import admin
from reservation.models import Reservation


class Reservations(admin.ModelAdmin):
    readonly_fields = ('cod_reservation',)
    list_display = ('id', 'cod_reservation', 'advertisement',
                    'price', 'check_in_date', 'check_out_date')


admin.site.register(Reservation, Reservations)
