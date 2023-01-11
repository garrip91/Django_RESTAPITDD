from rest_framework import serializers
from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """ENG: This class serializes the map of the model instance into JSON format."""
    """RUS: Этот класс сериализует отображение экземпляра модели в формате JSON."""
    
    class Meta:
        """ENG: This meta class is needed to map serializer's fields with the model fields."""
        """RUS: Этот метакласс сопоставляет поля сериализатора с полями модели."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

