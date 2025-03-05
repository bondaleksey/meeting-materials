import os
import threading

print(f"python process id: {os.getpid()}")

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f"At the moment python use: {total_threads} threads")

print(f"Name of current thread is: {thread_name}")
