from django.db import models

from houmer.models import Houmer, Property


class Visit(models.Model):
    property = models.ForeignKey(Property,
                                 related_name='visit', on_delete=models.PROTECT)
    houmer = models.ForeignKey(Houmer,
                               related_name='visit', on_delete=models.PROTECT)
    start_date = models.DateTimeField(blank=False, null=False)
    end_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.property.name, self.houmer.name)

    class Meta:
        app_label = 'houmer'
