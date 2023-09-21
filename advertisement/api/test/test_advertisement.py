from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from advertisement.models import Advertisement
from property.models import Property
from advertisement.api.factory.advertisement_factory import AdvertisementFactory
from property.api.factory.property_factory import Propertyactory


class PropertyAPITestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Advertisements-list')
        self.advertisement_1 = AdvertisementFactory()
        self.advertisement_2 = AdvertisementFactory()
        self.advertisement_3 = AdvertisementFactory()

    def test_list_advertisements(self):
        """
        Return status 200 and list of advertisement.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_advertisement(self):
        """
        Return status 201 and create a advertisement.
        """
        property = Propertyactory()
        data = {
            'property': property.id,
            'platform_name': 'Seazone',
            'platform_fee': 20
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Advertisement.objects.filter(
            property__id=data['property']).exists())

    def test_update_using_method_put_advertisement(self):
        """
        Return status 200 using method PUT and update a advertisement.
        """

        new_data = {
            'property': self.advertisement_3.property.id,
            'platform_name': 'Airbnb',
            'platform_fee': 20
        }
        url = f'{self.list_url}{self.advertisement_2.id}/'
        response = self.client.put(url, data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.advertisement_2.refresh_from_db()
        self.assertEqual(self.advertisement_2.property.id,
                         new_data['property'])
        self.assertEqual(self.advertisement_2.platform_name,
                         new_data['platform_name'])
        self.assertEqual(self.advertisement_2.platform_fee,
                         new_data['platform_fee'])

    def test_update_using_method_patch_advertisement(self):
        """
        Return status 200 using method PATCH and update a advertisement.
        """
        new_data = {
            'platform_name': 'Booking'
        }
        url = f'{self.list_url}{self.advertisement_1.id}/'
        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.advertisement_1.refresh_from_db()
        self.assertEqual(self.advertisement_1.platform_name,
                         new_data['platform_name'])

        self.assertEqual(self.advertisement_1.property.id, 1)
        self.assertEqual(self.advertisement_1.platform_fee, 30)

    def test_not_allowed_delete_advertisement(self):
        """
        Return status 204 not allowed.
        """
        url = f'{self.list_url}{self.advertisement_1.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
