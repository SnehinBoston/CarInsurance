from django.db import models
import datetime
from django.core.validators import MaxValueValidator
from payments.models import BasePayment

# Create your models here.
# Add more fields

class CarInsurance(models.Model):
    # class Meta:
    #     unique_together = ("make", "model", "year", "mileage")
    make = models.CharField(max_length = 100, verbose_name="Make")
    model = models.CharField(max_length = 30, verbose_name="Model")
    YEAR_CHOICES = [(r,r) for r in range(2000, datetime.date.today().year+1)]
    year = models.PositiveIntegerField(choices=YEAR_CHOICES, default = datetime.datetime.now().year, verbose_name="Year")
    mileage = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(1000000)], verbose_name="Mileage")

    def __str__(self):
        return "%s %s" %(self.make, self.model)

    def validate_unique(self, exclude=None):
        return super().validate_unique(exclude=None)
