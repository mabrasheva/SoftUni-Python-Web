from django.core.exceptions import ValidationError


def start_with_capital_letter_validator(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def contain_only_letters_validator(value):
    for letter in value:
        if not letter.isalpha():
            raise ValidationError("Plant name should contain only letters!")
