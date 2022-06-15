from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test.client import RequestFactory

# Create your tests here.
class LoginTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        new_user = User(username="Simon")
        new_user.set_password("1234")
        new_user.save()
    
    def test_login_registration(self):
        request = self.factory.get('/customer/details')
        yes = True
        try:
            user = authenticate(request, username="Simon", password="1234")
        except:
            yes = False
        self.assertEqual(yes, True)
