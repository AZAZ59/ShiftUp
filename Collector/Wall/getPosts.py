import pandas as pd
import datetime
from Utils import vkapi as vk


def get_posts_(owner_id, api, pool, count=None):
    posts_list = api.wall.get(**{'owner_id': owner_id, 'count': count if count else 100})
    if posts_list is None or posts_list <= 0:
        return pd.DataFrame()
    if count is None or count <= 100:
        return pd.DataFrame(posts_list[1:])
    count = posts_list[0]
    posts_list = pd.DataFrame(posts_list[1:])
    return posts_list.append(pool.map(lambda param: pd.DataFrame(api.wall.get(**param)[1:]), [
        {'owner_id': owner_id, 'count': 100 if count >= 100 else count, 'offset': offset}
        for offset in range(100, count, 100)
        ]), ignore_index=True).assign(timestamp=pd.to_datetime(datetime.datetime.utcnow()))


def get_posts(owner_ids, pool, count=None, token=None):
    api = vk.API((vk.Session(access_token=token) if token else vk.Session()))
    return pd.DataFrame().append(
            list(
                    map(
                            lambda owner_id: get_posts_(owner_id, api, pool, int(count) if count else count),
                            owner_ids
                    )
            ), ignore_index=True
    )
