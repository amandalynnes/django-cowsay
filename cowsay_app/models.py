from django.db import models

# Create your models here.


class TextItem(models.Model):
    text = models.CharField(max_length=350)

    def __str__(self):
        return f"{self.text}"
