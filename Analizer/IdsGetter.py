from multiprocessing.pool import ThreadPool

from  pandas import *

import Collector.config
from Collector.Groups import *
from Collector.Users import *


def getIdsToAnalyze(baseId:int, isUser: bool)->map :
    ids = {}
    with ThreadPool(450) as pool :
        if isUser :
            data = get_friends([baseId], pool, limit=2)
            for user in data :
                old = ids.get((user['uid'], True), {"id" : user['uid'], "user" : True, "count" : 0})
                old['count'] += 1
                ids[(user['uid'], True)] = old

            data = get_groups([baseId], pool)
            for gr in data :
                old = ids.get((gr['gid'], False), {"id" : gr['gid'], "user" : False, "count" : 0})
                old['count'] += 1
                ids[(gr['gid'], False)] = old
        else :
            data = get_all_members([baseId], pool)

            for user in data :
                old = ids.get((user['uid'], True), {"id" : user['uid'], "user" : True, "count" : 0})
                old['count'] += 1
                ids[(user['uid'], True)] = old
    return ids


def grownIdsToAnalyze(oldIds, deep=1) :
    newIds = oldIds.copy()
    count = len(oldIds)
    cur = 1
    for obj in oldIds :
        if cur % 10 == 0 :
            print(cur, str((cur / count) * 100) + "%")
        cur += 1

        id = obj[0]
        isUser = obj[1]
        ids = getIdsToAnalyze(id, isUser)

        for k, v in ids.items() :
            if k in newIds :
                newIds[k]['count'] += v['count']
            else :
                newIds[k] = v

    if deep == 1 :
        return newIds
    else :
        return grownIdsToAnalyze(newIds, deep - 1)
    pass


if __name__ == "__main__" :
    ids = getIdsToAnalyze('samarajs_look_ma_ima_developer', False)
    # ids = getIdsToAnalyze(28499999, True)
    ids=grownIdsToAnalyze(ids,1)
    df = DataFrame(ids)

    df = df.transpose()
    df = df.sort_values(by='count', ascending=False)

    print(df)

    pass
