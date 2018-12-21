import pandas as pd
import numpy as np
import time
import requests as requests
from progressbar import ProgressBar
import matplotlib.pyplot as plt
import itertools


def fetch(url):
    pbar = ProgressBar()
    posts = []
    after = None
    for i in pbar(range(40)):
        if after == None:
            params = {}
        else:
            params = {'after': after}

        headers = {'User-agent': 'Hunt'}
        res = requests.get(url, params=params, headers=headers)
        if res.status_code == 200:
            the_json = res.json()
            posts.extend(the_json['data']['children'])
            after = the_json['data']['after']
        else:
            print(res.status_code)
            break
        time.sleep(0.25)
        
    tmp_df_1 = pd.DataFrame(posts)
    tmp_list = []
    for post in tmp_df_1['data']:
        tmp_list.append(post)
        
    tmp_df_2 = pd.DataFrame(tmp_list)
    df = tmp_df_2[['subreddit', 'title', 'selftext']]
    
    return df



def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, fontsize = 15)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
         plt.text(j, i, format(cm[i, j], fmt),
                  horizontalalignment="center",
                  color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True' , fontsize = 12)
    plt.xlabel('Predicted', fontsize = 12)
    plt.tight_layout()
    