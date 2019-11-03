from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30, blank=True, default='')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
