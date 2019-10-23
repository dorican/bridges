from django.test import TestCase
from django.test.client import Client
from django.core.management import call_command

from .models import *


# Create your tests here.

class TestAuthappUrlsCase(TestCase):
    """ В этом тесте проверяем работоспособность страниц приложения Авторизации и коды ответа сервера """

    def setUp(self):
        self.client = Client()

    def test_authapp_urls(self):
        response = self.client.get('/auth/register/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/auth/profile/1/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/auth/profile/password_change/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/auth/profile/password_change_done/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/auth/logout/')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        call_command('sqlsequencereset', 'authapp')


class TestAuthappLoginCase(TestCase):
    """ В этом тесте мы проверяем авторизацию на сайте """

    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()
        self.superuser = Users.objects.create_superuser('django', 'info@pochta.ru', '123parol789')
        self.user = Users.objects.create_user('polzovatel', 'polzovatel@yandex.ru', '123polzovatel789')

    def test_user_login(self):
        # авторизация с правильными данными пользователя
        self.client.login(username='django', password='123parol789')
        response = self.client.get('/auth/login/')
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertContains(response, 'Вы авторизованы на сайте', status_code=200)
        self.client.get('/auth/logout/')

        # попытка авторизации с вымышленными данными
        self.client.login(username='nbhgftre', password='654kjh987')
        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertNotContains(response, 'Вы авторизованы на сайте', status_code=200)
        self.client.get('/auth/logout/')

    def tearDown(self):
        call_command('sqlsequencereset', 'authapp')
