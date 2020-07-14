from django.db import models

# Create your models here.

class Fake_info_pred(models.Model):
    link = models.CharField(max_length=220)


class Fake_info(models.Model):
    link = models.CharField(max_length=220)
    source = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
