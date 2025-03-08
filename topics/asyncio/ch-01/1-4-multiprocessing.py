import multiprocessing
import os


def hello_from_process():
    print(f"Hy from child process {os.getpid()}!")


if __name__ == "__main__":
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()

    print(f"Hy from Parent process {os.getpid()}")

    hello_process.join()
