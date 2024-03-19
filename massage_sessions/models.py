from django.db import models

from massage_masters.models import MassageMaster
from massage_types.models import MassageType


# Create your models here.


class MassageSession(models.Model):
    """"""
    session_types = (
        ('done', 'done'),
        ('processing', 'processing'),
        ('scheduled', 'scheduled'),
        ('canceled', 'canceled')
    )

    session_master = models.ForeignKey(MassageMaster, on_delete=models.DO_NOTHING, blank=True, null=True)
    session_type = models.ForeignKey(MassageType, on_delete=models.DO_NOTHING, blank=True, null=True)
    # session_client = models.ForeignKey(Client,  on_delete=models.DO_NOTHING, blank=True)
    client_name = models.CharField(max_length=20)
    client_phone = models.CharField()
    session_date = models.DateTimeField(blank=True, null=True)
    session_status = models.CharField(choices=session_types, default="processing")
    session_comment = models.TextField(max_length=200, blank=True, null=True)


    # def __str__(self):
    #     return self.name
