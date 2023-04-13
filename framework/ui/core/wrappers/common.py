import functools
import retrying


def retry_wrapper(*args, **kwargs):
    """
    Декоратор поверх retrying.retry(). Используется когда декорируемая функция не должна генерировать исключения.
    """

    def decorator(f):
        decorated = retrying.retry(*args, **kwargs)(f)

        @functools.wraps(decorated)
        def wrapper(*args, **kwargs):
            try:
                return decorated(*args, **kwargs)
            except retrying.RetryError:
                return False

        return wrapper

    if len(args) == 1 and callable(args[0]):
        return decorator(args[0])
    return decorator
