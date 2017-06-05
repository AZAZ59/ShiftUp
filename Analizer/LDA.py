from gensim import corpora
from gensim.models.ldamulticore import *
from Analizer.IdsGetter import *
from Collector.Wall import *
import Collector.config
import pickle

import re

def clean_str(string):
    """
    Tokenization/string cleaning for dataset
    Every dataset is lower cased except
    """
    string = re.sub(r"<.*>", "", string)
    string = re.sub(r"[^ A-Za-z0-9(),!?<>\'\`]", "", string)
    string = re.sub(r",", "", string)
    string = re.sub(r"!", "", string)
    string = re.sub(r"\(", "", string)
    string = re.sub(r"\)", "", string)
    string = re.sub(r"\?", "", string)
    string = re.sub(r"\s{2,}", " ", string)
    string = re.sub(r"[^A-Za-z ]", "", string)
    return string.strip().lower()

def downloadCorpus():
    regex = re.compile(r"<.*?>")
    ids = getIdsToAnalyze(28499999, True)
    corpus = []
    cur = 0
    count = len(ids)

    with ThreadPool(450) as pool :
        for k, v in ids.items() :
            if cur % 10 == 0 :
                print(cur, str((cur / count) * 100) + "%")
            cur += 1
            try :
                posts = get_posts((v['id'] * (1 if v['user'] else -1),), pool, 100)
                for post in posts :

                    corpus.append(clean_str(post['text']))
            except Exception as e :
                continue
    return corpus

if __name__ == "__main__" :

    print("make model")

    corpus=downloadCorpus()
    pickle.dump(corpus, open("texsts.bin", 'wb'))

    # corpus=pickle.load(open("texsts.bin",'rb'))

    texts = [[word for word in document.lower().split()] for document in corpus]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    pickle.dump((corpus,dictionary), open("corpus.bin", 'wb'))
    # (corpus,dictionary)=pickle.load(open("corpus.bin",'rb'))

    model = LdaModel(corpus=corpus,id2word=dictionary)
    model.save('model.bin')
    # model=LdaModel.load('model.bin')

    print(model)
    m=model.print_topics(100)
    for i in m:
        print(i)

