import time
import threading
import requests


def read_example() -> None:
    url = "https://www.example.com"
    response = requests.get(url)
    print(response.status_code)


thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)


thread_start = time.time()

thread_1.start()
thread_2.start()

print("All threads are working")

thread_1.join()
thread_2.join()

thread_end = time.time()

print(f"Multithreading execution takes {thread_end-thread_start} s.")
