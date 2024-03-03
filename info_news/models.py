from django.db import models

# Create your models here.


class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_content = models.TextField()
    news_date = models.DateField()

    def __str__(self):
        return self.news_title
