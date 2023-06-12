from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from my_music_app.web.validators import contains_only_allowed_symbols_validator


class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 15

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(MinLengthValidator(MIN_LEN_USERNAME), contains_only_allowed_symbols_validator,),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_LEN_ALBUM_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    R_N_B_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER = "Other"

    GENRES = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (R_N_B_MUSIC, R_N_B_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER, OTHER),
    )

    album_name = models.CharField(
        max_length=MAX_LEN_ALBUM_NAME,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Album Name",
    )

    artist = models.CharField(
        max_length=MAX_LEN_ARTIST,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        choices=GENRES,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL",
    )

    price = models.FloatField(
        validators=(MinValueValidator(0.0),),
        null=False,
        blank=False,
    )
