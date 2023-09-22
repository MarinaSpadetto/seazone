from rest_framework import serializers
from reservation.models import Reservation


class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        read_only_fields = ['cod_reservation']

    def validate(self, data):
        check_in_date = data.get('check_in_date')
        check_out_date = data.get('check_out_date')
        if check_in_date > check_out_date:
            raise serializers.ValidationError(
                {'check_in_date': 'The check-in date cannot be later than the check-out date.'})
        return data
