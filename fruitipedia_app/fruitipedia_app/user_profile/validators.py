from django.core.exceptions import ValidationError


def string_start_with_letter_validator(value):
    if not value[0].isalpha():
        raise ValidationError("Your name must start with a letter!")