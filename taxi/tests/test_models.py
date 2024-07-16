from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taxi.models import Manufacturer, Car


class ModelTests(TestCase):

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(
            name="Toyota",
            country="Japan"
        )
        self.assertEqual(
            str(manufacturer),
            f"{manufacturer.name} {manufacturer.country}"
        )

    def test_driver_str(self):
        driver = get_user_model().objects.create(
            username="testdriver",
            password="test123",
            first_name="Test",
            last_name="Driver",
            license_number="ABC123"
        )
        self.assertEqual(
            str(driver),
            f"{driver.username} ({driver.first_name} {driver.last_name})"
        )

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(
            name="Toyota",
            country="Japan"
        )
        car = Car.objects.create(model="Corolla", manufacturer=manufacturer)
        self.assertEqual(str(car), car.model)

    def test_create_driver_with_license_number(self):
        username = "testdriver"
        password = "test123"
        license_number = "ABC123"
        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            license_number=license_number,
        )
        self.assertEqual(driver.username, username)
        self.assertEqual(driver.license_number, license_number)
        self.assertTrue(driver.check_password(password))

    def test_get_absolute_url(self):
        driver = get_user_model().objects.create(
            username="testdriver",
            password="test123",
            first_name="Test",
            last_name="Driver",
            license_number="ABC123"
        )
        expected_url = reverse("taxi:driver-detail", kwargs={"pk": driver.pk})
        self.assertEqual(driver.get_absolute_url(), expected_url)
