from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
