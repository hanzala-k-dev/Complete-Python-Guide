"""
Shows basic threading examples and synchronization primitives in Python.
Includes comments and expected-output notes for learners to follow behavior.
"""

from time import sleep, time
import threading


# Simple worker function to simulate I/O-bound work
def task(thread_id):
    print(f"Sleeping... {thread_id}")
    sleep(1)  # simulate I/O wait
    print(f"Woke up... {thread_id}")


start_time = time()

# Create and start 10 threads that each sleep for ~1 second
threads = [threading.Thread(target=task, args=(i,)) for i in range(10)]
for t in threads:
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

end_time = time()
print(f"Main Thread Duration: {end_time - start_time} sec")
# Expected: ~1.0 - 1.2 seconds total because threads run concurrently


# THREAD SYNCHRONIZATION: avoiding race conditions with a Lock
balance = 200
lock = threading.Lock()


def deposit(amount, times, thread_lock):
    # safely increment shared balance 'times' times
    global balance
    for _ in range(times):
        thread_lock.acquire()
        balance += amount
        thread_lock.release()


def withdraw(amount, times, thread_lock):
    # safely decrement shared balance 'times' times
    global balance
    for _ in range(times):
        thread_lock.acquire()
        balance -= amount
        thread_lock.release()


# Start two threads that each modify balance many times; Lock prevents corruption
deposit_thread = threading.Thread(target=deposit, args=(1, 100000, lock))
withdraw_thread = threading.Thread(target=withdraw, args=(1, 100000, lock))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

print(f"Final Balance: {balance}")
# Expected: 200 (deposit and withdraw cancel out due to identical operations)
