from django.db import models


class Bucketlist(models.Model):
    """ENG: This class represents the model."""
    """RUS: Этот класс представляет модель записей (данных)."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """ENG: This method returns a human readable representation of the model instance."""
        """RUS: Этот метод возвращает удобочитаемое представление экземпляра модели."""
        return F"{self.name}"

