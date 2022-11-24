import csv
from io import StringIO

from rest_framework import serializers

from utils import db, misc

from .models import Billing, Service


class UploadSerializer(serializers.Serializer):
    upload_file = serializers.FileField()
    
    def create(self, validated_data):
        reader = csv.reader(
            StringIO(
                validated_data['upload_file'].file.read().decode()
            ), delimiter=','
        )
        invoices = misc.get_retrieve_data(reader)
        for invoice in invoices:
            db.save_data(invoice)
        return Billing


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name']


class BillingSerializer(serializers.ModelSerializer):
    customer = serializers.CharField(source='customer.name')
    company = serializers.CharField(source='company.name')
    services = ServiceSerializer(many=True)
    
    class Meta:
        model = Billing
        fields = [
            'customer', 'company', 'account', 'price', 'date', 'services'
        ]
