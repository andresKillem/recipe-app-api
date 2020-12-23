
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Creating new user with the email ok """
        email = 'test@london.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for a new user is normalized """
        email = "test@LONDON.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password="Asd123"
        )
        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email = None,
                password = "123"
            )

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            email = "andreco87@hotmail.com",
            password = "Asdqwe123."
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)    