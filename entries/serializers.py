from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('pk', 'site_name', 'site_url', 'login', 'password')

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.password = make_password(instance.password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        old_password = instance.password
        instance = super().update(instance, validated_data)
        self.update_password_if_changed(validated_data, instance, old_password)
        return instance

    @staticmethod
    def update_password_if_changed(validated_data, instance, old_password):
        new_password = make_password(instance.password) if old_password != validated_data['password'] else None
        if new_password:
            instance.password = new_password
            instance.save()
        return instance
