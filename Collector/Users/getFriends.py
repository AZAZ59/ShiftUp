#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from Utils import vkapi as vk
import pandas as pd
import datetime


def get_friends_(uid, token=None):
    api = vk.API((vk.Session(access_token=token) if token else vk.Session()))
    friends = api.friends.get(user_id=uid)
    if friends is None:
        return pd.DataFrame(columns=['uid_START', 'uid_END', 'timestamp'])
    return pd.DataFrame(friends, columns=['uid_END']).assign(
            uid_START=uid,
            timestamp=pd.to_datetime(datetime.datetime.utcnow())
    )


def get_friends(uids, pool, token=None):
    return pd.DataFrame().append(pool.map(lambda i: get_friends_(i, token), uids), ignore_index=True)


if __name__ == "__main__":
    pass


