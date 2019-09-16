from rest_framework import serializers
from customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
    password = serializers.CharField(required=False)
    username = serializers.CharField(required=False)
    email = serializers.EmailField(required=True)

    def create(self, validated_data):
        validated_data['username'] = validated_data['email']
        customer = Customer.objects.get_or_create(**validated_data)
        return customer[0]

    def __str__(self):
        return self.first_name