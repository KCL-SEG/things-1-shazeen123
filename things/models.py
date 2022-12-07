from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=40)
    description = models.CharField(unique=False, blank=True, max_length=150)
    quantity = models.IntegerField(
        unique=False,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)]
    )