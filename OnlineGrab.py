import vk
from itertools import chain
import sqlite3 as sqlite
import pandas as pd
import datetime
import time
from sqlalchemy import create_engine


def get_all_members(group_id, api):
    members_list = api.groups.getMembers(**{'group_id': group_id, 'count': 1000, 'fields':'online'})
    if members_list is None:
        return []
    data = map(lambda param: api.groups.getMembers(**param)['users'], [
        {'group_id': group_id, 'count': 1000, 'offset': offset, 'fields':'online'}
        for offset in range(1000, members_list['count'], 1000)
        ])
    return list(filter(lambda i: not i.get('deactivated', None), chain(*data, members_list['users'])))

#db_filename = 'users.db'
api = vk.API(vk.Session())
engine = create_engine('postgresql://postgres:123123@localhost:5432/postgres')

#with sqlite.connect(db_filename) as con:
while(True):
    try:
       print('start getiing:')
       data=pd.DataFrame(get_all_members(29627241, api))
       print('get ',len(data),' users')
       data['time']=[pd.to_datetime(datetime.datetime.today())]*len(data)
       data.to_sql('online', engine, if_exists='append', index=False)
       print('sleep')
       time.sleep(600)
       print('='*70)
    except Exception as e:
       print("!"*70)
       print(e)
       print("!"*70)
       time.sleep(600)
