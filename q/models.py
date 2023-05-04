from django.db import models

class Quiz(models.Model):
    topic = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return self.topic