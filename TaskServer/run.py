from multiprocessing.dummy import Pool as ThreadPool
from flask import Flask, jsonify, request
import flask_profiler
import Collector
import Analyzer
import Database
import json
import subprocess
import time
from itertools import chain


app = Flask(__name__)
pool = ThreadPool(450)

app.config["DEBUG"] = True
app.config["flask_profiler"] = {
    "verbose": True,
    "enabled": app.config["DEBUG"],
    "storage": {
        "engine": "sqlite"
    },
    "basicAuth": {
        "enabled": True,
        "username": "admin",
        "password": "admin"
    }
}


class Task:
    Collector = Collector
#    Analyzer = Analyzer


def parse_method(method_list, obj=Task):
    if len(method_list) > 0:
        method = method_list.pop(0)
        return parse_method(method_list, getattr(obj, method))
    else:
        return obj


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def gt(path):
    return """Home"""


@app.route('/task/<int:task_id>', methods=['GET'])
def task_post(task_id):
    try:
        with Database.session_scope() as session:
            task = session.query(Database.Task).get(task_id)
            params = json.loads(task.request)
            params['args']['pool'] = pool
            data = json.loads(
                    parse_method(params.get('method', '').split('.'))(**params.get('args', {})).to_json(orient='records'))
            task.state = 2
            date = time.time()
            if isinstance(data, list):
                session.add_all(
                        chain(
                                [
                                    Database.Result(task_id, json.dumps(result), date, part_id=i)
                                    for i, result in enumerate(data)
                                    ],
                                [task]
                        )
                )
            elif data is not None:
                task_result = Database.Result(task_id, data, date)
                session.add_all([task, task_result])
            else:
                session.add_all([task])
        return jsonify({'success': True,
                        'host':
                            subprocess.check_output("hostname", stderr=subprocess.STDOUT).
                       decode('utf-8').
                       replace('\n', '')})
    except Exception as ex:
        message = json.dumps({'values': [{
            'name': 'error',
            'value': 'Exception:{}, Parameters: {}'.format(ex.__class__, ex.__str__())
        }]},
                             ensure_ascii=False)
        print('---', ex)
        with Database.session_scope() as session:
            task = session.query(Database.Task).get(task_id)
            task.state = -1
            task_result = Database.Result(task_id, message, time.time())
            session.add_all([task, task_result])
        return message


@app.errorhandler(404)
def error_404(*args):
    print(str(subprocess.check_output("hostname", stderr=subprocess.STDOUT)))
    return jsonify({'success': False, 'error': 'Exception: {}'.format(404),
                    'host': subprocess.check_output("hostname", stderr=subprocess.STDOUT).decode('utf-8')
                   .replace('\n', '')})


@app.errorhandler(405)
def error_405(*args):
    print(str(subprocess.check_output("hostname", stderr=subprocess.STDOUT)))
    return jsonify({'success': False, 'error': 'Exception: {}'.format(405),
                    'host': subprocess.check_output("hostname", stderr=subprocess.STDOUT).decode('utf-8')
                   .replace('\n', '')})

flask_profiler.init_app(app)

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=6006, threaded=True)
    finally:
        pool.close()
        pool.join()
