import factory
from factory import Faker
from advertisement.models import Advertisement
from property.api.factory.property_factory import Propertyactory


class AdvertisementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Advertisement

    property = factory.SubFactory(Propertyactory)
    platform_name = Faker('random_element', elements=[
                          'Airbnb', 'Seazone', 'Booking'])
    platform_fee = 30
    created_at = Faker('date_between', start_date='-1y', end_date='now')
    updated_at = Faker('date_between', start_date='now', end_date='+1y')
