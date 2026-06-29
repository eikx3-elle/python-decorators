import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def retry(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            print(f"All {times} attempts failed")
        return wrapper
    return decorator

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.5)
    return a + b

@retry(times=3)
def unstable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("randomly failed")
    return "success"

@log
def multiply(a, b):
    return a*b

print("=== TIMER ===")
slow_add(3, 4)

print("\n=== RETRY ===")
unstable_function()

print("\n=== LOG ===")
multiply(5, 6)