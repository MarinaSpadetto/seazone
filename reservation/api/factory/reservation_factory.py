import factory
import uuid
from factory import Faker
from reservation.models import Reservation
from advertisement.api.factory.advertisement_factory import AdvertisementFactory


class ReservationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reservation

    cod_reservation = str(uuid.uuid4())
    advertisement = factory.SubFactory(AdvertisementFactory)
    check_in_date = '2023-09-20'
    check_out_date = '2023-10-20'
    price = 600
    comment = 'test of reservation'
    number_guests = 3
    created_at = Faker('date_between', start_date='-1y', end_date='now')
    updated_at = Faker('date_between', start_date='now', end_date='+1y')
