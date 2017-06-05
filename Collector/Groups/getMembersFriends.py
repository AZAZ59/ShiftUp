#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from Collector.Groups import get_members
from Collector.Users import get_friends


def get_members_friends(group_id: int, pool, token=None):
    return get_friends(get_members(group_id, pool, token)['uid'], pool, token)
