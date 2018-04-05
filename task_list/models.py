from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
