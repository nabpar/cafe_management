from django.db import models
from django.core.validators import RegexValidator

# Validators
def phone_no_validator():
    return RegexValidator(regex=r'^98\d{8}$|^97\d{8}$', message="Enter a valid mobile number")

def telephone_validator():
    return RegexValidator(regex=r'^0\d{1,2}\d{6,7}$', message="Enter a valid telephone number")

# Model
class CafeCms(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')
    email_1 = models.EmailField(verbose_name="E-mail", max_length=255, unique=True)
    email_2 = models.EmailField(verbose_name="E-mail", max_length=255, unique=True)
    email_3 = models.EmailField(verbose_name="E-mail", max_length=255, unique=True)
    mobile_no1 = models.CharField(max_length=10, validators=[phone_no_validator()], blank=True, null=True)
    mobile_no2 = models.CharField(max_length=10, validators=[phone_no_validator()], blank=True, null=True)
    mobile_no3 = models.CharField(max_length=10, validators=[phone_no_validator()], blank=True, null=True)
    telephone = models.CharField(max_length=10, validators=[telephone_validator()], blank=True, null=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
