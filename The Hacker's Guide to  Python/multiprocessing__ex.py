import multiprocessing
import random






def compute(n):
    return sum(
        [random.randint(1, 100) for i in range(1000000)]
    )

pool =multiprocessing.Pool(8)

print pool.map(compute, range(8))
