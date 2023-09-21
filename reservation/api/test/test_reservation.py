from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from reservation.models import Reservation
from reservation.api.factory.reservation_factory import ReservationFactory
from advertisement.api.factory.advertisement_factory import AdvertisementFactory


class PropertyAPITestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Reservations-list')
        self.reservation_1 = ReservationFactory()
        self.reservation_2 = ReservationFactory()
        self.reservation_3 = ReservationFactory()

    def test_list_reservations(self):
        """
        Return status 200 and list of reservations.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_reservation(self):
        """
        Return status 201 and create a reservation.
        """
        advertisement = AdvertisementFactory()
        data = {
            'advertisement': advertisement.id,
            'check_in_date': '2023-09-22',
            'check_out_date': '2023-09-26',
            'price': 100,
            'comment': 'test comment create a reservation',
            'number_guests': 4
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Reservation.objects.filter(
            advertisement__id=data['advertisement']).exists())

    def test_create_reservation_with_invalid_check_in_date(self):
        """
        Return status 400 and an error field.
        """
        advertisement = AdvertisementFactory()
        data = {
            'advertisement': advertisement.id,
            'check_in_date': '2023-09-25',
            'check_out_date': '2023-09-18',
            'price': 100,
            'comment': 'test comment create a reservation',
            'number_guests': 4
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            'The check-in date cannot be later than the check-out date.', str(response.data))

    def test_not_allowed_put_reservation(self):
        """
        Return status 204 not allowed.
        """
        advertisement = AdvertisementFactory()
        new_data = {
            'advertisement': advertisement.id,
            'check_in_date': '2022-12-20',
            'check_out_date': '2022-12-25',
            'price': 100,
            'comment': 'test update reservation ',
            'number_guests': 10
        }
        url = f'{self.list_url}{self.reservation_1.id}/'
        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(self.reservation_1.advertisement.id, 1)
        self.assertEqual(self.reservation_1.check_in_date, '2023-09-20')
        self.assertEqual(self.reservation_1.check_out_date, '2023-10-20')
        self.assertEqual(self.reservation_1.price, 600)
        self.assertEqual(self.reservation_1.comment, 'test of reservation')
        self.assertEqual(self.reservation_1.number_guests, 3)

    def test_not_allowed_patch_reservation(self):
        """
        Return status 204 not allowed.
        """
        new_data = {
            'number_guests': 2
        }
        url = f'{self.list_url}{self.reservation_2.id}/'
        response = self.client.patch(url, data=new_data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(self.reservation_2.number_guests, 3)

    def test_delete_reservation(self):
        """
        Return status 204.
        """
        url = f'{self.list_url}{self.reservation_3.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Reservation.DoesNotExist):
            Reservation.objects.get(id=self.reservation_3.id)
