from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from massage_types.models import MassageType


# Create your models here.


class MassageMaster(models.Model):
    """"""
    name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    about_master = models.TextField()
    master_experience = models.IntegerField()
    master_rating = models.FloatField(null=False, validators=[MinValueValidator(0.), MaxValueValidator(5.)])
    is_working = models.BooleanField(default=True)
    # master_foto = models.ImageField(upload_to='masters/', blank=True, null=True)
    master_types = models.ManyToManyField(MassageType, related_name="types", through="MasterType")

    def __str__(self):
        return f'{self.name} {self.last_name}'


class MasterType(models.Model):
    """"""
    master = models.ForeignKey(MassageMaster, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(MassageType, on_delete=models.DO_NOTHING)
