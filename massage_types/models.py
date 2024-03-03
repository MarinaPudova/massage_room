from django.db import models

# Create your models here.


class MassageType(models.Model):
    """"""
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    cost = models.FloatField()
    massage_cover = models.ImageField(upload_to='types/', blank=True, null=True)
    current_status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
