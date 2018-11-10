from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     RetrieveAPIView)
from rest_framework.permissions import AllowAny

from .serializers import EntrySerializer
from .models import Entry


class EntryView(RetrieveAPIView):
    model = Entry
    permission_classes = (AllowAny,)
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()


class ListEntryView(ListAPIView):
    model = Entry
    permission_classes = (AllowAny,)
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()


class CreateEntryView(CreateAPIView):
    model = Entry
    permission_classes = (AllowAny,)
    serializer_class = EntrySerializer


class UpdateEntryView(UpdateAPIView):
    model = Entry
    permission_classes = (AllowAny,)
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()


class DeleteEntryView(DestroyAPIView):
    model = Entry
    permission_classes = (AllowAny,)
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()
