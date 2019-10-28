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
        response = self.client.get('/auth/register/done/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/auth/logout/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/auth/profile/1/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/auth/profile/password_change/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/auth/profile/password_change_done/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/auth/profile/password_reset/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/auth/profile/password_reset/sent_mail/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/auth/profile/password_reset/complete/')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        call_command('sqlsequencereset', 'authapp')


class TestAuthappLoginLogoutCase(TestCase):
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

    def test_user_logout(self):
        # авторизуемся на сайте и разлогинимся
        self.client.login(username='django', password='123parol789')
        response = self.client.get('/auth/login/')
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertContains(response, 'Вы авторизованы на сайте', status_code=200)
        response = self.client.get('/auth/logout/')
        self.assertContains(response, 'Вы разлогинились', status_code=200)
        self.assertTrue(response.context['user'].is_anonymous)

        # разлогинимся без предварительной авторизации на сайте
        response = self.client.get('/auth/logout/')
        self.assertContains(response, 'Вы разлогинились', status_code=200)
        self.assertTrue(response.context['user'].is_anonymous)

    def tearDown(self):
        call_command('sqlsequencereset', 'authapp')


class AuthappRegistrationTestCase(TestCase):
    """ Проверяем регистрацию нового пользователя на сайте """

    def setUp(self):
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()
        self.superuser = Users.objects.create_superuser('django', 'info@pochta.ru', '123parol789')
        self.user = Users.objects.create_user('polzovatel', 'polzovatel@ya.ru', '123polzovatel789')

    def test_user_registration(self):
        # регистрация нового пользователя с корректными входными данными
        new_user = {'username': 'new_user', 'password': '123Parol789', 'phone': '+7(123)456-78-90'}
        response = self.client.post('/auth/register/', data=new_user)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/auth/register/done/')

        # попытка регистрации пользователя с ошибочными данными
        new_user = {'username': '1', 'password': '2', 'phone': '3'}
        response = self.client.post('/auth/register/', data=new_user)
        self.assertContains(response, 'Зарегистрироваться на сайте', status_code=200)

        # попытка повторной регистрации существующего пользователя
        new_user = {'username': 'polzovatel', 'password': '123polzovatel789', 'phone': '+7(123)456-78-90'}
        response = self.client.post('/auth/register/', data=new_user)
        self.assertContains(response, 'Зарегистрироваться на сайте', status_code=200)

        # попытка регистрации при авторизованном пользователе
        self.client.login(username='django', password='123parol789')
        response_login = self.client.get('/auth/login/')
        self.assertTrue(response_login.context['user'].is_authenticated)
        self.assertContains(response_login, 'Вы авторизованы на сайте', status_code=200)
        response_register = self.client.get('/auth/register/')
        self.assertContains(response_register, 'Вы уже авторизованы на сайте', status_code=200)
        self.client.get('/auth/logout/')

    def tearDown(self):
        call_command('sqlsequencereset', 'authapp')
