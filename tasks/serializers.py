from rest_framework import serializers
from .models import task

class taskserializer(serializers.ModelSerializer):
    class meta:
        model = task
        fileds = '__all__'

def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty or only spaces.")
        return value
    