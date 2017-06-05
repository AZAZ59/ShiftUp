import Database
from Collector.Groups import get_all_members
from functools import reduce
import time


def get_members_info(group_id, pool, members_list=None, do_return=False):
    members_list = members_list if members_list is not None \
        else get_all_members([group_id, ], pool, fields='online')
    print('GET mf')
    print(members_list)
    result = reduce(
            lambda res, x: (
                res[0] + x.get('online', 0),
                res[1] + (1 if x.get('deactivated', '') == 'banned' else 0),
                res[2] + (1 if x.get('deactivated', '') == 'deleted' else 0)
            ),
            members_list,
            (0, 0, 0)
    )
    date = time.time()
    with Database.session_scope() as session:
        session.add_all([Database.GroupMembersInfo(
                gid=group_id,
                count=len(members_list),
                online=result[0],
                banned=result[1],
                deleted=result[2],
                date=date
        )])
        if do_return:
            return dict(
                    gid=group_id,
                    count=len(members_list),
                    online=result[0],
                    banned=result[1],
                    deleted=result[2],
                    date=date
            )
