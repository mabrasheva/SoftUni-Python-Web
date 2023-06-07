from django.core.validators import MinValueValidator, MaxLengthValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    MIN_AGE = 12
    MAX_LEN_PASSWORD = 30
    MAX_LEN_FIRST_NAME = 30
    MAX_LEN_LAST_NAME = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        validators=(MinValueValidator(MIN_AGE),),
        null=False,
        blank=False,
    )
    password = models.CharField(
        validators=(MaxLengthValidator(MAX_LEN_PASSWORD),),
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
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return f"{self.first_name}"
        elif self.last_name:
            return f"{self.last_name}"
        else:
            return ""


class Game(models.Model):
    MAX_LEN_TITLE = 30
    MAX_LEN_CATEGORY = 15
    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD_GAME = "Board/Card Game"
    OTHER = "Other"
    MIN_RATING = 0.1
    MAX_RATING = 5.0
    MIN_LEVEL = 1

    CATEGORIES = (
        (ACTION, ACTION),
        (ADVENTURE, ADVENTURE),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_CARD_GAME, BOARD_CARD_GAME),
        (OTHER, OTHER),
    )

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        unique=True,
        null=False,
        blank=False,
    )
    category = models.CharField(
        max_length=MAX_LEN_CATEGORY,
        choices=CATEGORIES
    )
    rating = models.FloatField(
        validators=(MinValueValidator(MIN_RATING), MaxValueValidator(MAX_RATING),),
        null=False,
        blank=False,
    )
    max_level = models.IntegerField(
        validators=(MaxValueValidator(MIN_LEVEL),),
        null=True,
        blank=True,
        verbose_name="Max Level",
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL",
    )
    summary = models.TextField(
        null=False,
        blank=False
    )
