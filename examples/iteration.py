from contextlib import contextmanager
from multiprocessing import Process, Queue
import socket
import sqlite3
import time


with open('example.txt', 'r') as file:
    data = file.read()


data_to_write = input()
with open("example.txt", 'w') as file:
    file.write(data_to_write)


with open('example.txt', 'r') as file:
    data = file.read()


print(data)


##########

with socket.create_connection(("example.com", 80)) as connection:
    connection.sendall(b'Hello server!')
    data = connection.recv(1024)


print("Received data", data.decode("utf-8"))


##########

def get_data_from_db():
    with sqlite3.connect('example.sqlite3') as connection:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)

        cursor.execute(
            "INSERT INTO users (name, age) VALUES (?, ?)", ("John Doe", 25))
        cursor.execute(
            "INSERT INTO users (name, age) VALUES (?, ?)", ("Jane Smith", 30))
        connection.commit()


get_data_from_db()

##########


def worker_function(input_queue, output_queue):
    while True:
        data = input_queue.get()
        if data is None:
            break
        result = data * 2
        output_queue.put(result)


class MyProcessWrapper:
    def __enter__(self):
        self.input_queue = Queue()
        self.output_queue = Queue()

        self.process = Process(target=worker_function, args=(
            self.input_queue, self.output_queue))
        self.process.start()
        return self

    def __exit__(self, exc_type, ext_value, traceback):
        self.input_queue.put(None)
        self.process.join()


with MyProcessWrapper() as my_process:
    tasks = list(range(10))
    for task in tasks:
        my_process.input_queue.put(task)

    results = []
    for _ in tasks:
        result = my_process.output_queue.get()
        results.append(result)

    print("Results from process:", results)


##########

@contextmanager
def timing():
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    elapsed = end - start
    print(f"Elapsed time: {elapsed:.4f} seconds")

with timing():
    time.sleep(2)
