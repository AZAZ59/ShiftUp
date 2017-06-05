#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from Utils import vkapi as vk
import pandas as pd
import datetime


def get_members(group_id, pool, token=None):
    """Сбор подписчиков сообществ"""
    api = vk.API((vk.Session(access_token=token) if token else vk.Session()))
    members_list = api.groups.getMembers(group_id=group_id, count=1000)
    if members_list is None:
        return pd.DataFrame(columns=['uid', 'gid', 'timestamp'])
    res=pd.DataFrame(members_list['users'], columns=['uid'])
    if members_list['count']>1000:
        res.append(
           pool.map(
                            lambda param:pd.DataFrame(api.groups.getMembers(**param)['users'], columns=['uid']),
                            [
                                dict(group_id=group_id, count=1000, offset=offset)
                                for offset in range(1000, members_list['count'], 1000)
                            ]
                    )
                    , ignore_index=True
        ).assign(
            gid=group_id,
            timestamp=pd.to_datetime(datetime.datetime.utcnow())
    )
    return res


def get_all_members(group_ids, pool, limit=3,token=None):
    return pd.DataFrame().append(
        pool.map(
            lambda param: get_members(**param),
            [
                dict(group_id=group_id, pool=pool, token=token)
                for group_id in group_ids
            ]
        ),ignore_index=True)
