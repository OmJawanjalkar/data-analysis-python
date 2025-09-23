from concurrent.futures import ThreadPoolExecutor
import time

def fetch_data(n):
    print(f"Fetching data {n} ...")
    time.sleep(2)   # simulating I/O delay
    return f"Data {n}"

if __name__ == "__main__":
    start = time.time()

    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(fetch_data, [1, 2, 3, 4, 5]))

    print("Results:", results)
    print("Time taken:", time.time() - start)
