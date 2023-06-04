from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models

from car_collection_app.web.validators import min_len_username_validator, year_validator


class Profile(models.Model):
    MAX_LEN_USERNAME = 10
    MAX_LEN_PASSWORD = 30
    MAX_LEN_FIRST_NAME = 30
    MAX_LEN_LAST_NAME = 30
    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(min_len_username_validator,),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        validators=(MinValueValidator,),
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return f"{self.first_name}"
        elif self.last_name:
            return f"{self.last_name}"
        else:
            return ""


class Car(models.Model):
    MIN_MODEL_LENGTH = 2
    MAX_MODEL_LENGTH = 20
    MIN_PRICE = 1

    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        max_length=10,
        choices=CAR_TYPES,
        null=False,
        blank=False,
    )
    model = models.CharField(
        validators=(MinLengthValidator(MIN_MODEL_LENGTH), MaxLengthValidator(MAX_MODEL_LENGTH),),
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        validators=(year_validator,),
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(MIN_PRICE),),
    )
