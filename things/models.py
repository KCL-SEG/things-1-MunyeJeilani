from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


description_length_validator = RegexValidator(
    regex=r'^.{0,120}$', 
    message='Description must have a maximum of 120 characters.',
)

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(blank=True, validators=[description_length_validator])
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name