from django.db import models
from django.utils import timezone

# Create your models here.


class TextItem(models.Model):
    text = models.CharField(max_length=350)
    # time_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.text}"
