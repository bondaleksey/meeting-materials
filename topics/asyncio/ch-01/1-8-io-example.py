import time
import requests


def read_example() -> None:
    url = "https://www.example.com"
    response = requests.get(url)
    print(response.status_code)


sync_start = time.time()

read_example()
read_example()

sync_end = time.time()

print(f"Synchronous execution takes {sync_end-sync_start} s.")
