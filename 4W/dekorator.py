import time

def decorator(func):
    def wrap(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} returned: {result}")
        print(f"Execution time: {end - start:.6f} seconds")

        return result
    return wrap

@decorator
def multiply_numbers(x, y):
    return x * y

print(multiply_numbers(4, 5))
