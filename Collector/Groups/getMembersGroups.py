#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from Collector.Groups import get_members
from Collector.Users import get_groups


def get_members_groups(group_id, pool, token):
    return get_groups(get_members(group_id, pool, token)['uid'], pool, token)

