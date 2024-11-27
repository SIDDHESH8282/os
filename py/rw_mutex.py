import threading
import time
import random

# Shared resource
shared_data = []

# Mutex for synchronizing access to the shared resource
mutex = threading.Lock()

# Reader thread function
def reader(id):
    while True:
        time.sleep(random.randint(1, 3))  # Simulate reading time
        mutex.acquire()  # Lock the shared resource for reading
        print(f"Reader {id} is reading: {shared_data}")
        mutex.release()  # Release the lock after reading

# Writer thread function
def writer(id):
    while True:
        time.sleep(random.randint(2, 5))  # Simulate writing time
        data = random.randint(1, 100)  # Generate some random data to write
        mutex.acquire()  # Lock the shared resource for writing
        shared_data.append(data)
        print(f"Writer {id} wrote: {data}")
        mutex.release()  # Release the lock after writing

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

# Optionally, stop the threads after running for a while
# In a real-world scenario, you'd manage the thread termination properly
