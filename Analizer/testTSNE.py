#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from sklearn.cluster import AffinityPropagation

from Collector.Groups import get_members_groups
from Collector.Groups import get_all_members
from Collector.Users import  get_friends
import Collector.config
import numpy as np
from sklearn.manifold import TSNE, MDS
import matplotlib.pyplot as plt
from matplotlib import offsetbox
import pickle


def getShiftUp(filename, groupId) :
    from multiprocessing.dummy import Pool as ThreadPool
    with ThreadPool(450) as pool :
        data = get_members_groups(groupId, pool, limit=2)
        data.sort(key=lambda x : x['value'])
        users = [x['uid'] for x in get_all_members([groupId], pool=pool)]
        print(users)
        with open(filename, 'w') as f :
            f.write(','.join(['gid'] + [str(i) for i in users]))
            f.write("\n")
            for gr in data :
                print("us", gr)
                sr = ""
                sr += str(gr['gid']) + ","
                sr += ','.join(["1" if x in gr['users'] else "0" for x in users])
                f.write(sr + "\n")

def plot_embedding(X, title=None) :
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)

    plt.figure()
    ax = plt.subplot(111)

    cluster =AffinityPropagation(verbose=True)
    cluster.fit(X)

    for i in range(X.shape[0]) :
        if i % 10 == 0 :
            print("%d %%" % ((i / X.shape[0]) * 100))
        plt.text(X[i, 0], X[i, 1], '.', fontdict={'weight' : 'bold', 'size' : 9})
        # plt.text(X[i, 0], X[i, 1], str(cluster.predict(X[i])), fontdict={'weight' : 'bold', 'size' : 9})

    plt.xticks([]), plt.yticks([])
    if title is not None :
        plt.title(title)
    plt.savefig('fig1.svg')
    plt.show()


def transform(input, output, model=TSNE(n_components=2, random_state=0, verbose=5, n_iter=3000, learning_rate=500,
                                        n_iter_without_progress=3000),
              transponed=False
              ) :
    f = open(input)
    data = np.loadtxt(f, delimiter=',', skiprows=1, )
    data = data[: :][1 : :]

    if transponed:
        data=np.transpose(data)
        # newdata=np.zeros((data.shape[1],data.shape[0]))
        # for i in range(data.shape[0]):
        #     for j in range(data.shape[1]):
        #         if data[i][j]==1 :
        #             newdata[j][i]=1
        # data=newdata
    data_tsne = model.fit_transform(data)
    with open(output, 'wb') as out :
        pickle.dump((data_tsne, model.__dict__), out)


if __name__ == "__main__" :

    #29
    #+79539992244
    #+79171221874

    groupId="startupwarmup";
    filename = groupId+".csv"

    # getShiftUp(filename, filename[0:-4])

    getShiftUp(filename, groupId)
    print("Start transform")
    transform(filename, groupId + ".dat", transponed=True)
    print("End transform")

    with open('data.dat', 'rb') as file :
        data_tsne = pickle.load(file)
    plot_embedding(data_tsne, str("dghagkdjgask"))
    pass
