import threading


def hello_from_thread():
    print(f"Hello from thread {threading.current_thread()}!\n")


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name
print("{:d} threads are currently running\n".format(total_threads))
print(f"Name of current thread is: {thread_name}\n")

hello_thread.join()
