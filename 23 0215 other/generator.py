import time

start_time = time.perf_counter()
n = [n for n in range(10_000_000)] # List
duration = time.perf_counter() - start_time
print(f"List Comprehension:\t{duration:.6f} seconds")

start_time = time.perf_counter()
n = (n for n in range(10_000_000)) # Generator
duration = time.perf_counter() - start_time
print(f"Generator Expression:\t{duration:.6f} seconds")