from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}, {self.text}'