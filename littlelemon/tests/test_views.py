from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

User = get_user_model()

class MenuViewTest(TestCase):
    def setUp(self):
        # DRF test client
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass123!")
        self.client.force_authenticate(user=self.user)

        # Create a few Menu instances
        Menu.objects.create(title="Pizza", price=9.99, inventory=10)
        Menu.objects.create(title="Pasta", price=12.50, inventory=5)
        Menu.objects.create(title="Salad", price=7.25, inventory=20)

    def test_getall(self):
        # IMPORTANT: Use the correct URL for your menu list endpoint.
        # If you have a named url like name='menu', prefer reverse('menu').
        # Otherwise, use the hard-coded path.
        url = "/restaurant/menu/"  # <-- change if your endpoint differs

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Get all menu items from DB (same ordering as your view, if applicable)
        items = Menu.objects.all()
        serialized = MenuSerializer(items, many=True)

        # DRF Response has .data already parsed
        self.assertEqual(response.data, serialized.data)