from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    image = models.URLField(
        null=False,
        blank=False,
    )
    type = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
