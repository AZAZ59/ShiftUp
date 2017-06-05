import os
THREAD_COUNT_DEFAULT = 45
TASK_SERVER_BASE_URL = 'http://0.0.0.0:6006/task/{}'
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = 'sqlite:///'+os.path.join(basedir, 'app.db')