
# coding: utf-8

# In[4]:


#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import datetime, time, sys
import settings
import remake_csv as rc
import csv


# In[7]:


# 参考: http://ailaby.com/twitter_api/

# settingをする
session = OAuth1Session(
        settings.CONSUMER_KEY, 
        settings.CONSUMER_SECRET, 
        settings.ACCESS_TOKEN, 
        settings.ACCESS_TOKEN_SECRET)
 
url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
res = session.get(url, params = {'screen_name':'realDonaldTrump', 'count':300})
 
#--------------------
# ステータスコード確認
#--------------------
if res.status_code != 200:
    print ("Twitter API Error: %d" % res.status_code)
    sys.exit(1)
 
#--------------
# ヘッダー部
#--------------
print ('アクセス可能回数 %s' % res.headers['X-Rate-Limit-Remaining'])
print ('リセット時間 %s' % res.headers['X-Rate-Limit-Reset'])
sec = int(res.headers['X-Rate-Limit-Reset'])           - time.mktime(datetime.datetime.now().timetuple())
print ('リセット時間 （残り秒数に換算） %s' % sec)
 
#--------------
# テキスト部
#--------------
res_text = json.loads(res.text)
print(len(res_text))
data_list = []
b_time  = -100
for tweet in res_text:
    data = []
    data, b_time = rc.remake(tweet, b_time)
    
    if data != []:
        data_list.append(data)


# In[8]:


header_list = ["year", "month", "day", "hour","minute","t_time" "str_time", "retweeted_count", "favorite_count","category"]

try:
    filename = "abe_tweet.csv"
    with open(filename, 'w', newline='') as f:
        wrtr = csv.writer(f, delimiter=',')
        wrtr.writerow(header_list)
        #データを追加して保存する
        for data in data_list:
            wrtr.writerow(data)
        f.close()
except OSError as e:
    print('ファイル処理でエラー発生'.format(e.args))

