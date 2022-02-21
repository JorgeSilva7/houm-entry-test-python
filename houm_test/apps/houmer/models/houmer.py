from django.db import models
from django.conf import settings


class Houmer(models.Model):
    name = models.CharField("Name", max_length=240)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='houmer', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'houmer'
