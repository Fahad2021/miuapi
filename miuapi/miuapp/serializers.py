from rest_framework import serializers
from miuapp.models import Notice


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['title','Description','Date']