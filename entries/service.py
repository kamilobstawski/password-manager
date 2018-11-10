import datetime
import hashlib

from django.utils import timezone

from .models import Entry


def make_hash_value(entry, timestamp):
    hash = hashlib.sha256('{}'.format(str(entry.pk) + entry.password + entry.login + timestamp).encode())
    return hash.hexdigest()


def generate_link(entry_pk, request):
    http_host = 'http://' + request.META['HTTP_HOST']
    entry = Entry.objects.get(pk=entry_pk)
    timestamp = timezone.now().strftime('%y-%m-%d %H:%M')
    return http_host + '/temporary-entry/' + make_hash_value(entry, timestamp)


def check_token(token):
    timestamp_string = timezone.now().strftime('%y-%m-%d %H:%M')
    timestamp = datetime.datetime.strptime(timestamp_string, '%y-%m-%d %H:%M')
    for entry in Entry.objects.all():
        for i in range(5):
            hash = hashlib.sha256('{}'.format(str(entry.pk) + entry.password + entry.login +
                                              timestamp.strftime('%y-%m-%d %H:%M')).encode())
            if hash.hexdigest() == token:
                return entry.pk
            timestamp -= timezone.timedelta(minutes=1)
        timestamp += timezone.timedelta(minutes=5)
    return None
