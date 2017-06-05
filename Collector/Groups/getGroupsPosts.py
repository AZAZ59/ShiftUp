#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from Collector.Wall import get_posts
import numpy as np


def get_groups_posts(group_ids: list, pool, count=None, token=None):

    return get_posts(
            -1*np.array(group_ids),
            pool=pool,
            count=count if count is None else int(count),
            token=token
    )