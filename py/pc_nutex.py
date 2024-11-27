import threading
import time

BUFFER_SIZE = 5
MAX_ITEMS = 5

buffer = [None] * BUFFER_SIZE
in_index = 0
out_index = 0
produced_count = 0
consumed_count = 0

mutex = threading.Lock()
full = threading.Condition(mutex)
empty = threading.Condition(mutex)

def producer():
    global produced_count, in_index
    item = 1

    while produced_count < MAX_ITEMS:
        with mutex:
            while (in_index + 1) % BUFFER_SIZE == out_index:
                empty.wait()  # Wait until there is space in the buffer

            buffer[in_index] = item
            print(f"Produced: {item}")
            item += 1
            in_index = (in_index + 1) % BUFFER_SIZE

            produced_count += 1

            full.notify()  # Notify the consumer that the buffer has a new item

def consumer():
    global consumed_count, out_index
    while consumed_count < MAX_ITEMS:
        with mutex:
            while in_index == out_index:
                full.wait()  # Wait until there is an item to consume

            item = buffer[out_index]
            print(f"Consumed: {item}")
            out_index = (out_index + 1) % BUFFER_SIZE

            consumed_count += 1

            empty.notify()  # Notify the producer that there is space in the buffer

def main():
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

if __name__ == "__main__":
    main()
