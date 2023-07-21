from django.core.exceptions import ValidationError


def validate_word_count(value):
    max_word_count = 100
    words = value.split()
    if len(words) > max_word_count:
        raise ValidationError("Please limit the text to a maximum of 100 words.")


def validate_digits_only(value):
    if not value.isdigit():
        raise ValidationError('Contact number must contain only digits.')
