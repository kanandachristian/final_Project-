from django.db import models
from django.urls import reverse
# Create your models here.


class Rate(models.Model):
    Rwandan = models.DecimalField(
        max_digits=19, decimal_places=2, db_index=True)
    congolese = models.DecimalField(
        max_digits=19, decimal_places=2, db_index=True)
    Usd = models.DecimalField(max_digits=19, decimal_places=2, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
