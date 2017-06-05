#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from Collector.Groups.getAllMembers import get_members
from Collector.Groups.getAllMembers import get_all_members
from Collector.Groups.getGroupsInfo import get_groups_info
from Collector.Groups.getMembersFriends import get_members_friends
from Collector.Groups.getGroupsPosts import get_groups_posts
from Collector.Groups.getMembersGroups import get_members_groups


def _get_glb():
    return globals()
