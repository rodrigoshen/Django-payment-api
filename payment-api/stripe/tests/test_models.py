from django.test import TestCase

from ..models import Account

class AccountTestCase(TestCase):
    def test_set_str_name_model(self):
        account = Account(username="testuser", name="Test User", email="testuser@example.com", password="testpassword")
        self.assertEqual(str(account), "O nome da conta é testuser")


