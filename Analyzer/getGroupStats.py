from Collector.Likes import get_user_activity
from Collector.Groups import get_groups_info
from Analyzer import get_members_info


def get_group_stats(group, pool):
    print('Get group info')
    group = get_groups_info(group_ids=[group], fields='screen_name,name,photo_100', pool=pool)[0]
    print(group)
    print('Get members info')
    info = get_members_info(group_id=group['gid'], do_return=True, pool=pool)
    print(info)
    print('Get user activity')
    activity = get_user_activity(owner_id=-group['gid'], do_return=True, pool=pool)
    group['photo'] = group.pop('photo_100')
    group['values'] = [dict(name=key, value=value) for key, value in info.items()]
    return group
