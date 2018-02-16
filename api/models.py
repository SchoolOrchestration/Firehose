from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

class Payload(models.Model):

    path = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)

    get = JSONField(default={})
    post = JSONField(default={})
    tags = ArrayField(models.CharField(max_length=100), default=[], blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_date = models.DateTimeField(auto_now=True, db_index=True)
