#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import pandas as pd
import datetime
from Utils import vkapi as vk


def get_groups_(uid, pool, token):
    print(uid)
    api = vk.API(vk.Session(access_token=token))
    group_list = api.groups.get(user_id=uid, count=1000)
    if group_list is None:
        group_list = api.users.getSubscriptions(user_id=uid, count=1)
        if group_list is None:
            return pd.DataFrame(columns=['uid', 'gid', 'timestamp'])
        count = group_list.get('users', {}).get('count')
        return pd.DataFrame(
                filter(
                        lambda x: x['type'] == 'page',
                        pool.map(
                                lambda param: api.users.getSubscriptions(**param),
                                [
                                    {'user_id': uid, 'count': 200,  'extended': 1, 'offset': offset}
                                    for offset in range(0, count, 200)
                                    ]
                        )
                ),
                columns=['gid']).assign(uid=uid, timestamp=pd.to_datetime(datetime.datetime.utcnow()))
    res = pd.DataFrame(group_list[1:], columns=['gid'])
    if group_list[0]>1000:
        res.append(
                    pool.map(
                            lambda param: pd.DataFrame(api.groups.get(**param)[1:], columns=['gid']),
                            [
                                {'user_id': uid, 'count': 1000, 'offset': offset}
                                for offset in range(1000, group_list[0], 1000)
                                ]
                    ), ignore_index=True).assign(uid=uid, timestamp=pd.to_datetime(datetime.datetime.utcnow()))
    return res


def get_groups(uids, pool, token):
    return pd.DataFrame().append(pool.map(lambda i: get_groups_(i, pool, token), uids), ignore_index=True)
