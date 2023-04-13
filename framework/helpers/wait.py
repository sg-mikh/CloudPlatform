import time


def wait_while(func, timeout=10):
    """
    Ждет до тех пор, пока переданная функция не вернет позитивное значние, либо не сработает таймаут
    """
    timer = 0
    while not func():
        if timer >= timeout:
            return False
        time.sleep(1)
        timer += 1
    return func()
