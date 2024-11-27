import threading
import time
import random

# Shared resource
shared_data = []

# Semaphore to control access
mutex = threading.Semaphore(1)  # For mutual exclusion of writers
readers_count = threading.Semaphore(1)  # To protect readers_count

# To count the number of readers currently accessing the resource
reader_count = 0

# Reader thread function
def reader(id):
    global reader_count
    while True:
        time.sleep(random.randint(1, 3))  # Simulate reading time
        readers_count.acquire()  # Lock the reader count
        reader_count += 1
        if reader_count == 1:  # First reader locks the mutex
            mutex.acquire()
        readers_count.release()  # Release the reader count lock

        # Reading shared data
        print(f"Reader {id} is reading: {shared_data}")

        readers_count.acquire()  # Lock the reader count
        reader_count -= 1
        if reader_count == 0:  # Last reader releases the mutex
            mutex.release()
        readers_count.release()  # Release the reader count lock

# Writer thread function
def writer(id):
    while True:
        time.sleep(random.randint(2, 5))  # Simulate writing time
        data = random.randint(1, 100)  # Generate random data to write
        
        mutex.acquire()  # Only one writer can write at a time
        shared_data.append(data)
        print(f"Writer {id} wrote: {data}")
        mutex.release()  # Release the mutex after writing

# Create reader and writer threads
readers = [threading.Thread(target=reader, args=(i,)) for i in range(1, 4)]
writers = [threading.Thread(target=writer, args=(i,)) for i in range(1, 3)]

# Start the threads
for r in readers:
    r.start()

for w in writers:
    w.start()

# Let the threads run for some time
time.sleep(20)
