from re import sub


def camel_to_snake(camel_str):
    snake_str = sub(r'([a-z])([A-Z])', r'\1_\2', camel_str)
    return snake_str.lower()
