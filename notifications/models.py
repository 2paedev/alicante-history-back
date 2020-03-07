from django.db import models


class Notification(models.Model):
    deviceId = models.CharField(primary_key=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=150, blank=False, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.token}'
