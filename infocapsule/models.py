from django.db import models

# Create your models here.

class NewsProvider(models.Model):
    name = models.CharField(max_length=200, blank=False)
    main_url = models.CharField(max_length=500, blank=False)
    