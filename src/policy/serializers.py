from rest_framework import serializers
from policy.models import Policy, CustomerPolicy

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = '__all__'

    def create(self, validated_data):
        policy = Policy.objects.get_or_create(**validated_data)
        return policy[0]


class CustomerPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPolicy
        fields = '__all__'

    def create(self, validated_data):
        customer_policy = CustomerPolicy.objects.get_or_create(**validated_data)
        return customer_policy[0]