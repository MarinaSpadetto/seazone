import factory
from factory import Faker
from factory import Sequence
from property.models import Property


class Propertyactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Property

    cod_property = Sequence(lambda n: f"FCT00{n}")
    limit_guests = 6
    quantity_bathroom = 2
    allowed_pets = True
    cleaning_fee = 80.00
    activation_date = '2023-09-18'
    created_at = Faker('date_between', start_date='-1y', end_date='now')
    updated_at = Faker('date_between', start_date='now', end_date='+1y')
