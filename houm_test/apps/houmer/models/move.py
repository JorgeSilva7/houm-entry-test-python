from django.db import models

from django.db.models import JSONField
from houmer.models import Houmer, Property


class Move(models.Model):
    property_destination = models.ForeignKey(Property,
                                             related_name='move', on_delete=models.PROTECT)
    houmer = models.ForeignKey(Houmer,
                               related_name='move', on_delete=models.PROTECT)
    start_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=True, null=True)
    start_coordinates = JSONField(default=dict, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.houmer.name, self.property_destination.name)

    class Meta:
        app_label = 'houmer'
