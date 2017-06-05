#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from itertools import chain
import datetime
import pandas as pd
from Collector.config import GROUPS_FIELDS
from Utils import vkapi as vk


def get_groups_info(group_ids, pool, fields=GROUPS_FIELDS, token=None):
    api = vk.API((vk.Session(access_token=token) if token else vk.Session()))
    request_set = [', '.join([str(y) for y in group_ids[i:i+500]]) for i in range(0, len(group_ids), 500)]
    return pd.DataFrame().append(pool.map(lambda param: pd.DataFrame(api.groups.getById(**param)), [
        dict(group_ids=group_ids, fields=fields)
        for group_ids in request_set
        ], ignore_index=True).assign(timestamp=pd.to_datetime(datetime.datetime.utcnow())))




