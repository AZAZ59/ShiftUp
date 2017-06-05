import requests
from Database.config import TASK_SERVER_BASE_URL
import Database
from time import sleep
from multiprocessing.dummy import Pool as ThreadPool
from Database.config import THREAD_COUNT_DEFAULT


def get_new_tasks_ids(session):
    return session.query(Database.Task).filter(Database.Task.state == 0).all()


def send_task(task):
    try:
        task.state = 1
        response = requests.get(TASK_SERVER_BASE_URL.format(task.id), timeout=(0.33, 0.33))
        print("task {}".format(task.id), response)
    except requests.exceptions.ReadTimeout:
        print('Oops. Read timeout occured')
    except requests.exceptions.ConnectTimeout:
        print('Oops. Connection timeout occured!')
    except requests.exceptions.ConnectionError:
        print('Oops. Connection error occured!')
        sleep(1)
    finally:
        return task


def main(pool):
    while True:
        with Database.session_scope() as session:
            new_tasks = get_new_tasks_ids(session)
            session.add_all(list(pool.map(send_task, new_tasks)))
            sleep(0.33)

if __name__ == "__main__":
    pool = ThreadPool(THREAD_COUNT_DEFAULT)
    try:
        main(pool)
    except Exception:
        sleep(2)
        main(pool)
    finally:
        pool.close()
        pool.join()


