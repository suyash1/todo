from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
    title = serializers.CharField(max_length=30, required=True)
    # description = serializers.CharField(max_length=500, required=False)

    def create(self, validated_data):
        task = Task.objects.get_or_create(**validated_data)
        return task[0]

