from django.test import TestCase
from django.utils import timezone

from entries.test_factory import EntryFactory
from entries import service


class GenerateLinkToolsTest(TestCase):
    def test_make_hash_value(self):
        entry = EntryFactory()
        self.assertIsNotNone(service.make_hash_value(entry, timezone.now()))

    def test_generate_link(self):
        entry = EntryFactory()
        self.assertIsNotNone(service.generate_link(entry.pk))

    def test_correct_token_generated_now(self):
        [EntryFactory() for i in range(10)]
        entry = EntryFactory()
        token = service.make_hash_value(entry, timezone.now())
        self.assertEqual(service.check_token(token), entry.pk)

    def test_correct_token_generated_four_minutes_ago(self):
        entry = EntryFactory()
        timestamp = timezone.now() - timezone.timedelta(minutes=4)
        token = service.make_hash_value(entry, timestamp)
        self.assertEqual(service.check_token(token), entry.pk)

    def test_invalid_token_after_six_minutes(self):
        entry = EntryFactory()
        timestamp = timezone.now() - timezone.timedelta(minutes=6)
        token = service.make_hash_value(entry, timestamp)
        self.assertIsNone(service.check_token(token))
