import threading
import time
import random


def get_data(task_id, sem):
    print(f"processing get_data({task_id})")
    time.sleep(random.randint(1, 3))
    sem.release()
    print(f"completed get_data({task_id})")


def write_to_file(task_id, sem):
    print(f"processing write_to_file({task_id})")
    time.sleep(random.randint(1, 5))
    sem.release()
    print(f"completed write_to_file({task_id})")


def write_to_console(task_id, sem):
    print(f"processing write_to_console({task_id})")
    time.sleep(random.randint(1, 5))
    sem.release()
    print(f"completed write_to_console({task_id})")


tasks_id = [_ for _ in range(1, 21)]
threading.Thread(ta)