from sqlalchemy import create_engine, update
from Database.config import DATABASE_URL
from Database.models import *
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
engine = create_engine(DATABASE_URL, echo=True, connect_args={'check_same_thread': False})
Base.metadata.bind = engine


def get_session():
    return sessionmaker(bind=engine)()


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = get_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.expunge_all()
        session.close()

if __name__ == "__main__":
    """
    import inspect

    def get_func_args(func):
        args = {}
        for key, value in inspect.signature(func).parameters.items():
            show = key not in ['pool', 'token']
            if value.default.__class__ == type.__class__:
                required = True
                arg_type = value.annotation.__name__
            else:
                required = False
                arg_type = type(value.default).__name__
            args.update({key: {'required': required, 'type': arg_type, 'show': show}})
        return args

    import Collector
    import types
    from itertools import chain
    funcs = []
    for mod in ('Groups', 'Users'):
        funcs.append([('Collector.{}.{}'.format(mod, key), get_func_args(value), value.__doc__ if value.__doc__ is not None else key[0].capitalize()+key.replace('_', ' ')[1:])
                      for key, value in getattr(Collector, mod)._get_glb().items()
                      if key[0] != '_' and isinstance(value, types.FunctionType)])
    """
    Base.metadata.create_all(engine)
    """
    with session_scope() as session:
        base_data = [Method(func[0], func[1], method_list=0, title=func[2]) for func in chain(*funcs)]
        session.add_all(base_data)"""

