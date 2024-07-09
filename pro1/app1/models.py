from django.db import models
from django.core import validators

#necked function
def check(nm):
    if nm.istitle()!=True:
        raise validators.ValidationError('Please Enter First Letter in UpperCase.')

# Create your models here.
class Bank(models.Model):
    bid = models.IntegerField(primary_key=True,
                              validators=[validators.MinValueValidator(1),
                                          validators.MaxValueValidator])
    name = models.CharField(max_length=34,
                            validators=[check])
    email = models.CharField(max_length=34,
                             validators=[validators.RegexValidator(
                                 '^[A-Za-z0-9].+[@]{1}[a-zA-Z].+[.]{1}com|in|gov|co$'
                             )])
    mob = models.CharField(max_length=34,
                           validators=[validators.RegexValidator(
                               '^([+]\\d{2}[ ])?\\d{10}$'
                           )])
    adhar = models.CharField(max_length=34,
                             validators=[validators.RegexValidator(
                                 '^[0-9]{4}[ ]?[0-9]{4}[ ]?[0-9]{4}$'
                             )])
    pan = models.CharField(max_length=34,
                           validators=[validators.RegexValidator(
                               '^[A-Z]{3}[PCAFHT]{1}[A-Z]{1}[0-9]{4}[A-Z]{1}$'
                           )])
    accno = models.CharField(max_length=34,
                             validators=[validators.RegexValidator(
                                 '^\\d{9,18}$'
                             )])
    ifsc = models.CharField(max_length=34,
                            validators=[validators.RegexValidator(
                                '^[A-Z]{4}0[A-Z0-9]{6}$'
                            )])
    gender = models.CharField(max_length=34)
    dob = models.DateField()
    profile_pic = models.ImageField(upload_to='profile')