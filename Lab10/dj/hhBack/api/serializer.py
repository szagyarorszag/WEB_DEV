from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, min_length=1)
    description = serializers.CharField()
    city = serializers.CharField(max_length=255, min_length=1)
    address = serializers.CharField(max_length=255, min_length=1)

    def create(self, data): return Company.objects.create(data)

    def update(self, instance, data):
        instance.name = data.get('name', instance.name)
        instance.description = data.get('description', instance.description)
        instance.city = data.get('city', instance.city)
        instance.address = data.get('address', instance.address)
        instance.save()
    def delete(self, instance): instance.delete()


class VacancySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255, min_length=1)
    description = serializers.CharField()
    salary = serializers.FloatField(allow_null=True)
    company = CompanySerializer()

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company')
