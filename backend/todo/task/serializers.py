from rest_framework import serializers
from .models import DirectoryModel, TaskModel


class DirectorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectoryModel
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    directory = serializers.SerializerMethodField()

    def get_directory(self, instance):
        return {
            'id': instance.directory.id if instance.directory else "",
            'title': instance.directory.title if instance.directory else ""
        }

    class Meta:
        model = TaskModel
        fields = '__all__'


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'
