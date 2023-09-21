from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from property.models import Property
from property.api.factory.property_factory import Propertyactory


class PropertyAPITestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Properties-list')
        self.property_1 = Propertyactory()
        self.property_2 = Propertyactory()
        self.property_3 = Propertyactory()

    def test_list_properties(self):
        """
        Return status 200 and list of properties.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_property(self):
        """
        Return status 201 and create a property.
        """
        data = {
            'cod_property': 'TST012',
            'limit_guests': 4,
            'quantity_bathroom': 1,
            'allowed_pets': False,
            'cleaning_fee': '100.00',
            'activation_date': '2023-09-19'
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Property.objects.filter(
            cod_property=data['cod_property']).exists())

    def test_update_using_method_put_property(self):
        """
        Return status 200 using method PUT and update a property.
        """
        new_data = {
            'cod_property': 'TST053',
            'limit_guests': 5,
            'quantity_bathroom': 2,
            'allowed_pets': True,
            'cleaning_fee': '110.00',
            'activation_date': '2023-09-19'
        }
        url = f'{self.list_url}{self.property_2.id}/'
        response = self.client.put(url, data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.property_2.refresh_from_db()
        self.assertEqual(self.property_2.cod_property,
                         new_data['cod_property'])
        self.assertEqual(self.property_2.limit_guests,
                         new_data['limit_guests'])
        self.assertEqual(self.property_2.quantity_bathroom,
                         new_data['quantity_bathroom'])
        self.assertEqual(self.property_2.allowed_pets,
                         new_data['allowed_pets'])
        self.assertEqual(self.property_2.activation_date.strftime('%Y-%m-%d'),
                         new_data['activation_date'])

    def test_update_using_method_patch_property(self):
        """
        Return status 200 using method PATCH and update a property.
        """
        new_data = {
            'allowed_pets': False
        }
        url = f'{self.list_url}{self.property_1.id}/'
        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.property_1.refresh_from_db()
        self.assertEqual(self.property_1.allowed_pets,
                         new_data['allowed_pets'])

        self.assertEqual(self.property_1.cod_property, 'FCT009')
        self.assertEqual(self.property_1.limit_guests, 6)
        self.assertEqual(self.property_1.quantity_bathroom, 2)
        self.assertEqual(self.property_1.cleaning_fee, 80)
        self.assertEqual(self.property_1.activation_date.strftime(
            '%Y-%m-%d'), '2023-09-18')

    def test_delete_property(self):
        """
        Return status 204.
        """
        url = f'{self.list_url}{self.property_3.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Property.DoesNotExist):
            Property.objects.get(id=self.property_3.id)
