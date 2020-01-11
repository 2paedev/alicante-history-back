from django.db import models


class Bibliography(models.Model):
    description = models.CharField(max_length=350, blank=True, default='')

    class Meta:
        ordering = ['description']

    def __str__(self):
        return self.description
