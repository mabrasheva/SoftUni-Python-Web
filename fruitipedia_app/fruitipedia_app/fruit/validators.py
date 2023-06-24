from django.core.exceptions import ValidationError


def string_contain_only_letter_validator(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError("Fruit name should contain only letters!")