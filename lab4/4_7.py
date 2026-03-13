def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция {func.__name__} с args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(5, 7))
