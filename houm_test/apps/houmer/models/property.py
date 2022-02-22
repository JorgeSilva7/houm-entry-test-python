from django.db import models

from django.db.models import JSONField
from houmer.models import Houmer


class Property(models.Model):
    name = models.CharField("Name", max_length=240)
    houmer = models.ForeignKey(Houmer,
                               related_name='property', on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    coordinates = JSONField(default=dict, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.name, self.houmer.name)

    class Meta:
        app_label = 'houmer'
