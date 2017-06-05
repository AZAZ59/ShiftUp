from multiprocessing.pool import ThreadPool

from pandas import DataFrame

from Collector.Users import get_friends

id=960323
with ThreadPool(450) as pool :
    data = get_friends([id], pool, limit=2,fields='city')
    df = DataFrame(data)
    # df = df.transpose()
    print(df.groupby('city').count())