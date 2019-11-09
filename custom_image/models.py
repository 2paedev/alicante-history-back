from django.db import models


class CustomImage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=True, default='')
    url = models.ImageField(upload_to='', blank=False, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
