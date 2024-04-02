from rest_framework import serializers
from .models import (CustomUser,Product)
from django.contrib.gis.geos import Point
from .models import CustomUser, UserRole


class UserSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=UserRole.choices)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email','phone_no','password','role']
        read_only_fields = ['id']


class PointFieldSerializer(serializers.Field):
    def to_representation(self, value):
        return {
            "type": "Point",
            "coordinates": [value.x, value.y]
        }
    def to_internal_value(self, data):
        return Point(data['coordinates'][0], data['coordinates'][1])

class ProductSerializer(serializers.ModelSerializer):
    location = PointFieldSerializer()
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'quantity', 'location', 'category','user']