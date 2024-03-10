from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from massage_masters.models import MassageMaster


# Create your models here.


class ClientComment(models.Model):

    content = models.TextField(blank=True, null=True)
    #  TODO вариант для выбора числа из предложенных вариантов рассмотреть InteregChoise
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True, editable=True)

    master = models.ForeignKey(MassageMaster, on_delete=models.CASCADE, related_name='comments')
    # client = models.ForeignKey(MassageClient, related_name='comments')

    class Meta:
        ordering = ('-created_at',)
        