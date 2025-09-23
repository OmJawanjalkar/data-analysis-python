from concurrent.futures import ProcessPoolExecutor
import time

def compute_square(n):
    print(f"Computing square of {n}")
    time.sleep(2)   # simulating heavy computation
    return n * n

if __name__ == "__main__":
    start = time.time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(compute_square, [1, 2, 3, 4, 5]))

    print("Results:", results)
    print("Time taken:", time.time() - start)
