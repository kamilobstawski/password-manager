from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from entries.models import Entry
from entries.test_factory import EntryFactory


class ListEntryViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='admin', password='test12345')
        self.client.force_login(user)

    def test_listing(self):
        EntryFactory()
        response = self.client.get(reverse('entries:entries'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)
        self.assertEqual(1, len(response.data))


class GetEntryViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='admin', password='test12345')
        self.client.force_login(user)

    def test_get(self):
        entry = EntryFactory()
        response = self.client.get(reverse('entries:get_entry', args=[entry.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)


class CreateEntryViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='admin', password='test12345')
        self.client.force_login(user)

    def test_valid_creation(self):
        data = {
            'site_name': 'google',
            'site_url': 'https://www.google.com/login/',
            'login': 'admin',
            'password': 'test12345'
        }
        self.client.login()
        response = self.client.post(reverse('entries:create_entry'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data)
        self.assertEqual(len(Entry.objects.all()), 1)


class UpdateEntryViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create(username='admin', password='test12345')
        self.client.force_login(user)

    def test_valid_update(self):
        entry = EntryFactory()
        data = {
            'site_name': 'google.com',
            'site_url': 'https://www.google.com/login/',
            'login': 'admin',
            'password': 'test12345'
        }
        response = self.client.put(reverse('entries:update_entry', args=[entry.pk]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Entry.objects.get(pk=entry.pk).site_name, data['site_name'])


class DeleteEntryViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='admin', password='test12345')
        self.client.force_login(user)
        
    def test_listing(self):
        entry = EntryFactory()
        self.assertEqual(len(Entry.objects.all()), 1)
        response = self.client.delete(reverse('entries:delete_entry', args=[entry.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Entry.objects.all()), 0)
