from Utils import vkapi as vk
import pandas as pd
import datetime
from Collector.config import MEMBERS_FIELDS


def get_users_info(user_ids, pool, fields=MEMBERS_FIELDS, token=None):
    api = vk.API((vk.Session(access_token=token) if token else vk.Session()))
    request_set = [', '.join([str(y) for y in user_ids[i:i+1000]]) for i in range(0, len(user_ids), 1000)]
    return pd.DataFrame().append(pool.map(lambda param: pd.DataFrame(api.users.get(**param)), [
        dict(user_ids=user_ids, fields=fields)
        for user_ids in request_set
        ], ignore_index=True).assign(timestamp=pd.to_datetime(datetime.datetime.utcnow())))

