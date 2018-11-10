from django.test import TestCase

from entries.models import Entry


class EntryModelTest(TestCase):
    def setUp(self):
        self.entry = Entry.objects.create(
            site_name='Sentry',
            site_url='https://sentry.io/password-manager/',
            login='admin',
            password='test12345'
        )

    def test_valid_creation(self):
        self.assertEqual(Entry.objects.all().exists(), True)

    def test_institution_data(self):
        self.assertEqual(self.entry.site_name, 'Sentry')
        self.assertEqual(self.entry.site_url, 'https://sentry.io/password-manager/')
        self.assertEqual(self.entry.login, 'admin')
        self.assertEqual(self.entry.password, 'test12345')
