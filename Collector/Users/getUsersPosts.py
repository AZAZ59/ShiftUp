#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from Collector.Wall import get_posts


def get_users_posts(user_ids, pool, count=None, token=None):
    return get_posts(user_ids, pool, count if not count else int(count), token)

