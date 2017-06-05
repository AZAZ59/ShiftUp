from Utils import vkapi as vk
import pandas as pd
import datetime


def get_likes(owner_id, post_id, pool, pfilter='likes', ptype='post', token=None):
    api = vk.API((vk.Session(access_token=token) if token else vk.Session()))
    likes = api.likes.getList(type=ptype, owner_id=owner_id, item_id=post_id, count=1000, filter=pfilter)
    if likes is None:
        return pd.DataFrame()
    count = likes.get('count', 0)
    if count == 0:
        return pd.DataFrame()
    return pd.DataFrame(likes).append(pool.map(
            lambda param: pd.DataFrame(api.likes.getList(**param)),
            [
                dict(type=ptype, owner_id=owner_id, item_id=post_id, count=1000, filter=pfilter, offset=offset)
                for offset in range(1000, count, 1000)
                ]
    ), ignore_index=True).assign(rate=lambda x: 1/x.count, timestamp=pd.to_datetime(datetime.datetime.utcnow()))


def get_comments(owner_id, post_id, pool, token=None):
    api = vk.API((vk.Session(access_token=token) if token else vk.Session()))
    comments = api.wall.getComments(owner_id=owner_id, post_id=post_id, count=100)
    if comments is None:
        return pd.DataFrame()
    count = comments[0]
    if count == 0:
        return pd.DataFrame()
    return pd.DataFrame(comments[1:]).append(pool.map(
            lambda param: pd.DataFrame(api.likes.getList(**param)[1:]),
            [
                dict(owner_id=owner_id, post_id=post_id, count=100, offset=offset)
                for offset in range(100, count, 100)
                ]
    ), ignore_index=True).assign(count=count, rate=1/count, timestamp=pd.to_datetime(datetime.datetime.utcnow()))


