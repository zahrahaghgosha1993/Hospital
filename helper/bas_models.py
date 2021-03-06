import uuid
from django.db import models


class AbstractModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True,default=uuid.uuid4, auto_created=True, editable=False)
    updated = models.DateTimeField(null=True, auto_now=True)
    created = models.DateTimeField(null=True, auto_now_add=True)

