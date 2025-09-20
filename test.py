import time

def wrapper(func):
    def Timer():
        start = time.perf_counter()  # Correctly call perf_counter()
        result = func()  # Call the decorated function
        end = time.perf_counter()
        time_func = end - start  # Calculate elapsed time
        print(time_func)
        return result  # Return the actual result of the function
    return Timer

@wrapper
def hi():
    return "hello"

print(hi())  # Call the decorated function and print its result
