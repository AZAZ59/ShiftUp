
import pandas as pd
import numpy as np
from multiprocessing.dummy import Pool as ThreadPool
from Utils import vkapi as vk

pool = ThreadPool(450)
DEFAULT_TOKEN = '5eed487cbd3f61ac8f53581a06906edf3fb6019cb65051b69977abac6ce7672c446a688754c34fa3b6a18'
api = vk.API(vk.Session(access_token=DEFAULT_TOKEN))


# In[2]:

def count_user_groups(uid):
    group_list = api.groups.get(**{'user_id': uid, 'count': 100})
    #print(group_list)
    if group_list is None:
        group_list = api.users.getSubscriptions(**{'user_id': uid, 'count': 1})
        if group_list is None:
            return dict(user=str(uid), groups=None)
        #print(uid, group_list.get('users', {}).get('count'))
        return dict(user=str(uid), groups=group_list.get('users', {}).get('count'))
    #print(uid, group_list[0])
    return dict(user=str(uid), groups=group_list[0])


# In[ ]:

i=0
while(True):
    l = 1000
    user_ids = np.random.randint(1, 41800000, l)

    user_groups = pd.DataFrame(
        list(
            pool.map(count_user_groups, user_ids)
        )
    )
    #user_groups = user_groups.dropna()
    user_groups.to_csv('{}ug{}.csv'.format(len(user_ids),i))
    i+=1
    print('='*25,i)
