import sys
import random
import numpy as np
from numba import jit
import time


@jit(nopython=True)
def main_numba(u, r):
    a = np.zeros(10000, dtype=np.int64)  # Array of 10k elements initialized to 0
    for i in range(10000):  # 10k outer loop iterations
        for j in range(100000):  # 100k inner loop iterations, per outer loop iteration
            a[i] += j % u  # Simple sum
        a[i] += r  # Add a random value to each element in array
    return a[r]  # Return a single element from the array


def main(u, r):
    a = [0] * 10000  # Array of 10k elements initialized to 0
    for i in range(10000):  # 10k outer loop iterations
        for j in range(100000):  # 100k inner loop iterations, per outer loop iteration
            a[i] += j % u  # Simple sum
        a[i] += r  # Add a random value to each element in array
    return a[r]  # Return a single element from the array


u = int(sys.argv[1])  # Get an input number from the command line
r = random.randint(0, 10000)  # Get a random number 0 <= r < 10k

for func, descr in [(main, "Looping"), (main_numba, "Numba")]:
    start_time = time.time()
    result = func(u, r)
    end_time = time.time()

    print(f"Result: {result}")
    print(f"Execution Time with {descr}: {end_time - start_time} seconds")

