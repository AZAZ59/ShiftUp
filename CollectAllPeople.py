
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from multiprocessing.dummy import Pool as ThreadPool

from Utils import vkapi as vk
# import vk as vk
from itertools import chain
import time
from sqlalchemy import create_engine
import sqlalchemy as sa
import warnings
import pickle

warnings.simplefilter('ignore')

api = vk.API(vk.Session())


# In[2]:

def get_delta(user):
    last_seen=user.pop('last_seen').get('time', 0)
    user['time'] = int(time.time()-last_seen)
    return user
 
def get_users(uids):
    return filter(lambda i: i['time'] < 2678400,
                  map(get_delta, filter(
        lambda i: (not 'deactivated' in i),
        api.users.get(user_ids=uids, fields='last_seen')
    )))
 
users = lambda user_ids, pool: pd.DataFrame(
    list(
        chain(
            *pool.map(get_users, user_ids.reshape((int(l/1000), 1000)))
        )
    )   
)
engine = create_engine('postgresql://postgres:123123@localhost:5432/postgres') 

def write_to_db(df, fr,to):   
    st_time = time.time()
    print('\n===== start from:{} to:{}'.format(fr,to))

    metadata = sa.MetaData()

    widgets_table = sa.Table('users', metadata,
        sa.Column('uid', sa.Integer)
    )
    
    values = df.values
    values = list(values.reshape(1,len(values)))[0]
    with engine.connect() as connection:
        with connection.begin() as transaction:
            try:
                s='INSERT INTO users VALUES '
                s1='('+'),('.join(map(str,values))+')'
                s=s+s1
                #print(s)
                connection.execute(s)
            except:
                transaction.rollback()
                raise
            else:
                transaction.commit()
    print('\n===== end   from:{} to:{}'.format(fr,to))
    print('Write to db time: {} sec.'.format(int(time.time()-st_time)))


# In[4]:

l = 1000000
steps = np.arange(0, 518000000-l, l)
counts=[]
pgPool=ThreadPool(50)

with ThreadPool(777) as pool:
    for step in steps:
        print('-------')
        print('Time: {} '.format(time.asctime( time.localtime(time.time()) )))
        st_time = time.time()
        step += 1
        user_ids = np.arange(step, step+l, 1)
        user_list = users(user_ids, pool).uid
        if len(user_list)==0:
            break
        print('From {:,}'.format(user_ids[0]))
        print('To {:,}'.format(user_ids[l-1]))       
        print('Size: {:,}'.format(len(user_list)))    
        print('Elapsed time: {} sec.'.format(int(time.time()-st_time)))

        st_time = time.time()
        counts.append(len(user_list))
        print('Write to array {} sec.'.format(int(time.time()-st_time)))
        print('-------')
#         await writeToDB(user_list)
        
        pgPool.apply_async(write_to_db,(user_list,user_ids[0],user_ids[l-1]))
#        write_to_db(user_list,user_ids[0],user_ids[l-1])
        
#         user_list.to_sql('users_all_test', engine,if_exists='append', index=False)
# time.sleep(600)
pgPool.close()
pgPool.join()

with open('qwe,pickle','wb') as file:
    pickle.dump(counts,file)
    


# In[ ]:



