from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from helper.bas_models import AbstractModel
from helper.model_validator import validate_phone


class Patient(AbstractModel,):
    name = models.CharField(max_length=100, null=True,blank=True)
    last_name = models.CharField(max_length=100, null=True,blank=True)
    disease = models.CharField(max_length=100, null=True,blank=True)
    phone = models.CharField(verbose_name=_('phone'),
                             validators=[validate_phone],
                             max_length=15, unique=True, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)


