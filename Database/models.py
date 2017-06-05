from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Float
from flask_bcrypt import generate_password_hash, check_password_hash
import json
Base = declarative_base()


class _BaseMixin(object):
    def save(self, Session):
        Session.add(self)
        Session.commit()

    def delete(self, Session):
        Session.delete(self)
        Session.commit()


class PendingTask(Base, _BaseMixin):
    __tablename__ = 'pending_tasks'

    id = Column(Integer, ForeignKey('tasks.id'), primary_key=True, nullable=False, unique=True)
    request = Column(String, nullable=False)

    def __init__(self, id, request):
        self.id = id
        self.request = request if isinstance(request, str) else json.dumps(request)

    def get_attr_dict(self):
        return {
            'id': self.id,
            'request': self.request
        }


class Task(Base, _BaseMixin):
    __tablename__ = 'tasks'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    creator_id = Column(Integer, nullable=False)
    request = Column(String, nullable=False)
    state = Column(Integer)
    # title = Column(String)

    def __init__(self, creator_id, request, state, title=''):
        self.creator_id = creator_id
        self.request = request
        self.state = state
        # self.title = title

    def get_attr_dict(self):
        return {
            'id': self.id,
            'creator_id': self.creator_id,
            'request': self.request,
            'state': self.state
        }


class Result(Base, _BaseMixin):
    __tablename__ = 'tasks_results'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    result_id = Column(Integer, ForeignKey('tasks.id'))
    result = Column(String)
    part_id = Column(Integer)
    date = Column(Float, nullable=False)

    def __init__(self, result_id, result, date, part_id=0):
        self.result_id = result_id
        self.result = result if isinstance(result, str) else json.dumps(result)
        self.part_id = part_id
        self.date = date

    def get_attr_dict(self):
        return {
            'id': self.id,
            'result_id': self.result_id,
            'result': self.result,
            'part_id': self.part_id,
            'date': self.date
        }


class User(Base, _BaseMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    token = Column(String)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    def __init__(self, id, email, password, token=''):
        self.id = id
        self.email = email
        self.password = self.hash_password(password)
        self.token = token


class Method(Base, _BaseMixin):
    __tablename__ = 'methods'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String, nullable=False)
    args = Column(String, nullable=False)
    title = Column(String)
    list = Column(Integer)

    def __init__(self, name, args, method_list=0, title=''):
        self.name = name if isinstance(name, str) else json.dumps(name)
        self.args = args if isinstance(args, str) else json.dumps(args)
        self.list = method_list
        self.title = title


class GroupMembersInfo(Base, _BaseMixin):
    __tablename__ = 'group_members_info'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    gid = Column(Integer, nullable=False)
    online = Column(Integer)
    banned = Column(Integer)
    deleted = Column(Integer)
    count = Column(Integer)
    date = Column(Float)

    def __init__(self, gid, count, online, banned, deleted, date):
        self.gid = gid
        self.count = count
        self.banned = banned
        self.date = date
        self.online = online
        self.deleted = deleted

    def get_attr_dict(self):
        return dict(
                gid=self.gid,
                count=self.count,
                online=self.online,
                banned=self.banned,
                deleted=self.deleted,
                date=self.date
        )


class WallActivity(Base, _BaseMixin):
    __tablename__ = 'wall_activity'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    owner_id = Column(Integer, nullable=False)
    user_id = Column(Integer)
    rate = Column(Float)
    likes_rate = Column(Float)
    copies_rate = Column(Float)
    comments_rate = Column(Float)
    likes = Column(Integer)
    copies = Column(Integer)
    comments = Column(Integer)
    date = Column(Float)

    def __init__(self, owner_id, user, rate, likes_rate, copies_rate, comments_rate, likes, copies, comments, date):
        self.owner_id = owner_id
        self.user_id = user
        self.date = date
        self.rate = rate
        self.likes_rate = likes_rate
        self.copies_rate = copies_rate
        self.comments_rate = comments_rate
        self.copies = copies
        self.likes = likes
        self.comments = comments

    def get_attr_dict(self):
        return dict(
                owner_id=self.owner_id,
                user_id=self.user_id,
                rate=self.rate,
                likes_rate=self.likes_rate,
                copies_rate=self.copies_rate,
                comments_rate=self.comments_rate,
                likes=self.likes,
                copies=self.copies,
                comments=self.comments,
                date=self.date
        )


class WatchingGroups(Base, _BaseMixin):
    __tablename__ = 'watching_groups'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    user_id = Column(Integer)
    group_id = Column(Integer)

    def __init__(self, user_id, group_id):
        self.user_id = user_id
        self.group_id = group_id

