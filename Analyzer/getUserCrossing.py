def get_user_crossing(data, limit):
    result = {}
    for user in data:
        uid = user['uid']
        if uid not in result.keys():
            result[uid] = {'value': 1, 'user': user}
        else:
            result[uid]['value'] += 1
        result[uid]['user']['values'] = [dict(name="Пересечение", value=result[uid]['value'])]
    return sorted(
            [
                value.get('user')
                for key, value in result.items() if (value.get('value', 0) >= int(limit))
                ], key=lambda x: 0 if not isinstance(x, dict) else -x.get('values', [{}])[0].get('value', 0))
