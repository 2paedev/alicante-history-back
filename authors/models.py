from django.db import models


class Author(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, blank=True, default='')
    surname = models.CharField(max_length=50, blank=True, default='')
    email = models.CharField(max_length=50, blank=True, default='')
    image = models.ImageField(upload_to='', blank=False, null=False)
    description = models.CharField(max_length=10000, blank=False, null=False, default='')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} {self.surname}'
