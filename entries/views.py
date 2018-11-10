import json

from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from django.core import serializers
from rest_framework.generics import (ListAPIView,
                                     CreateAPIView,
                                     DestroyAPIView,
                                     UpdateAPIView,
                                     RetrieveAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import EntrySerializer
from .models import Entry
from . import service


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


class GenerateLink(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, entry_pk):
        link = service.generate_link(entry_pk, request)
        return Response({'link': link})


class TemporaryEntryView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, token):
        entry_pk = service.check_token(token)
        entry = get_object_or_404(Entry, pk=entry_pk)
        dict_obj = model_to_dict(entry)
        return Response(dict_obj)
