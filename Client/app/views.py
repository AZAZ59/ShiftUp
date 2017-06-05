from Client.app import app
from flask import render_template, request, jsonify
import Database


@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def index(path):
    return render_template('index.html')


@app.route('/api/task', methods=['POST'])
def create_task():
    with Database.session_scope() as session:
        task = Database.Task(creator_id=0, request=request.data.decode("utf-8"), state=0)
        task.save(session)
    return 'success'


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    with Database.session_scope() as session:
        tasks = session.query(Database.Task).order_by(-Database.Task.id).limit(100)
        return jsonify(
                [
                    task.get_attr_dict()
                    for task in tasks
                ]
        )


@app.route('/api/tasks/<int:result_id>', methods=['GET'])
def get_result_by_id(result_id):
    with Database.session_scope() as session:
        results = session.query(Database.Result)\
            .filter(Database.Result.result_id == result_id)\
            .order_by(Database.Result.part_id).limit(100)
        return jsonify(
                       [result.get_attr_dict() for result in results]
        )


@app.route('/api/groups', methods=['GET'])
def get_groups_lists():
    with Database.session_scope() as session:
        group_ids = session.query(Database.WatchingGroups.group_id).\
            filter(Database.WatchingGroups.user_id == 0).all()


@app.route('/api/groups/<int:group_id>', methods=['GET'])
def get_group(group_id):
    with Database.session_scope() as session:
        if group_id not in session.query(Database.WatchingGroups.group_id)\
                .filter(Database.WatchingGroups.user_id == 0).all():
            jsonify(dict(type='error', values=[dict(name='Ошибка', value='Ошибка доступа')]))
        else:
            members_info = session.query(Database.GroupMembersInfo).\
                filter(Database.GroupMembersInfo.gid == group_id).\
                order_by(-Database.GroupMembersInfo.id).limit(2)
            return members_info


