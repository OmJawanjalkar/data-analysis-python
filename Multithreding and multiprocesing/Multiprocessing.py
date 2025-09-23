import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")

if __name__ == "__main__":
    # Create 2 processes
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_number)

    t = time.time()   # start timer

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to complete
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(f"⏳ Total time taken: {finished_time:.2f} seconds")
