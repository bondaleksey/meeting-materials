import time
import multiprocessing
import requests


def read_example() -> None:
    url = "https://www.example.com"
    response = requests.get(url)
    print(response.status_code)


# Точка входа для multiprocessing: Код, создающий и запускающий процессы,
# должен находиться внутри блока if name == "main":. Без этого могут
# возникнуть проблемы с рекурсивным созданием процессов, особенно в Windows.

if __name__ == "__main__":

    process_1 = multiprocessing.Process(target=read_example)
    process_2 = multiprocessing.Process(target=read_example)

    process_start = time.time()

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    process_end = time.time()

    print(f"Multiprocessing execution takes {process_end-process_start} s.")
