from django.core.exceptions import ValidationError


def min_len_username_validator(value):
    if len(value) < 2:
        raise ValidationError('The username must be a minimum of 2 chars')


def year_validator(value):
    if value < 1980 or value > 2049:
        raise ValidationError("Year must be between 1980 and 2049")
