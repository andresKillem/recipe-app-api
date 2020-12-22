from django.test import TestCase, Client
from django.contrib.auth import get_user_model
#Allow us to generate urls for admin pages
from django.urls import reverse
#Allow us to make request

class AdminSiteTests(TestCase):
    #SetUp function is a function that runs before every test that run
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_super_user(
            email = "andreco87@hotmail.com",
            password = "Asdqwe123."
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="normal@user.com",
            password="Asd123",
            name = "TestUser"
        )
        return super().setUp()


    def test_user_listed(self):
        """Test that users are listed in the user page  """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertTrue(res.status_code, "200")
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_chage_page(self):
        """ Test that the user edit page works """
        #Create the url
        url = reverse('admin:core_user_change', args=[self.user.id])
        # Reverse will create something like /admin/core/user/1
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)