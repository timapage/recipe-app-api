from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_email_successfull(self):
        """Test user with email created successfully"""
        email = "ochilov_temur1997@mail.ru"
        password = "ytrewq321"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_new_normalized_user(self):
        """Test if user is normalized"""
        email = 'ochilov_temur1997@MAIL.RU'
        user = get_user_model().objects.create_user(email, 'etst123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_email_validation(self):
        """ Test if user entered email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_superuser(self):
        """ Test if superuser created successfully"""
        user = get_user_model().objects.create_superuser(
            'ochilov_temur1997@mail.ru',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
