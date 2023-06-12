import re

from django.core.exceptions import ValidationError


def contains_only_allowed_symbols_validator(value):
    if not re.match("^\w+$", value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
