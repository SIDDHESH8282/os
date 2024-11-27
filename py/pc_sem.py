import threading
import time

BUFFER_SIZE = 5
MAX_ITEMS = 10

buffer = [None] * BUFFER_SIZE
in_index = 0
out_index = 0
produced_count = 0
consumed_count = 0

mutex = threading.Semaphore(1)
full = threading.Semaphore(0)
empty = threading.Semaphore(BUFFER_SIZE)

def producer():
    global produced_count, in_index
    item = 1

    while produced_count < MAX_ITEMS:
        empty.acquire()  # Wait if the buffer is full
        mutex.acquire()  # Lock access to the buffer

        buffer[in_index] = item
        print(f"Produced: {item}")
        item += 1
        in_index = (in_index + 1) % BUFFER_SIZE

        produced_count += 1

        mutex.release()  # Release the lock
        full.release()  # Signal the consumer that an item is available

def consumer():
    global consumed_count, out_index
    while consumed_count < MAX_ITEMS:
        full.acquire()  # Wait if the buffer is empty
        mutex.acquire()  # Lock access to the buffer

        item = buffer[out_index]
        print(f"Consumed: {item}")
        out_index = (out_index + 1) % BUFFER_SIZE

        consumed_count += 1

        mutex.release()  # Release the lock
        empty.release()  # Signal the producer that space is available

def main():
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

if __name__ == "__main__":
    main()
    
