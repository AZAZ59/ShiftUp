
# coding: utf-8

# In[1]:

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
    user_groups.to_csv('{}ug{}.csv'.format(len(user_ids),))


# In[ ]:

# Python 2 and 3 compatibility
# pip install future
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
# отключим предупреждения Anaconda
import warnings
warnings.simplefilter('ignore')
user_groups = user_groups.dropna()

# будем отображать графики прямо в jupyter'e
get_ipython().magic('pylab inline')
import seaborn as sns


sns.distplot(user_groups.groups)


# In[ ]:

'Mean',user_groups.groups.mean(), 'Std', user_groups.groups.std(), 'Var',user_groups.groups.var()


# In[ ]:

import matplotlib.pyplot as plt
fig=plt.figure()
plt.hist(user_groups.groups)


# In[ ]:

zero_g = [c for c in user_groups.groups if c==0]
m = user_groups.groups.max()
max_g = [c for c in user_groups.groups if c==m]
l = [c for c in user_groups.groups if c>=385]
round(len(zero_g)/len(user_groups.groups)*100, 2), round(len(max_g)/len(user_groups.groups)*100, 2), round(len(l)/len(user_groups.groups)*100, 2)


# In[ ]:

cols=['user', 'groups']
#user_groups = pd.read_csv('1000ug.csv')
sns_plot = sns.jointplot(x="user", y="groups", data=user_groups)
sns_plot.savefig('pairplot.png')
user_groups[cols].plot()


# In[ ]:

df = user_groups[user_groups.groups > 0]#[user_groups.groups < 200]
sns_plot = sns.jointplot(x="user", y="groups", data=df, kind="kde", space=0, color="g")
sns_plot.savefig('pairplot_without_zero.png')


# In[ ]:

user_groups[user_groups.groups >= 380]

