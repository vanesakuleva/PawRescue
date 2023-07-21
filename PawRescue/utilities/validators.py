from django.core.exceptions import ValidationError


def validate_word_count(value):
    max_word_count = 200
    words = value.split()
    if len(words) > max_word_count:
        raise ValidationError("Please limit the text to a maximum of 200 words.")

