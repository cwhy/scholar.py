from __future__ import print_function
import scholar as gs
import time
import pandas as pd
from random import betavariate


querier = gs.ScholarQuerier()
q = gs.SearchScholarQuery()

df = pd.read_csv('JPE.csv')
titles = df.Title

output = df.iloc[0:20]
titles = titles[0:20]
# for _title in titles:


def query(_title):
    time.sleep(betavariate(2, 2)/2)  # to prevent overrequesting Google's server
    q.set_phrase(_title)
    querier.send_query(q)
    q_title = querier.articles[0].attrs['title'][0]
    q_num_cit = querier.articles[0].attrs['num_citations'][0]
    print((q_title, q_num_cit))
    return (q_title, q_num_cit)

(output['q_title'], output['q_num_cit']) = zip(*titles.map(query))
output.to_csv('JPE2.csv')
