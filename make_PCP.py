
# coding: utf-8

# In[5]:


import csv
import urllib.request
import zipfile
import os
import tori_time


# In[6]:


# リンクデータ
# ダウンロード先HP
# http://www.mujinzou.jp/
# http://souba-data.com/k_data/年/NS_年月/NSL_年月日
def make_url(year, month, day):
    # 一桁の場合リンクが取れないので0をつける
    str_m = str(month).zfill(2)
    str_d = str(day).zfill(2)

    return "http://souba-data.com/k_data/" + str(year) + "/NS_" + str(year)[2:] + str_m + "/NSL_" + str(year)[2:] + str_m + str_d + ".zip"

# DEBUG
#print(make_url(2019,10, 5))


# In[7]:


# CSVファイルを取得する
def getCSVFile(year, month, day):
    str_m = str(month).zfill(2)
    str_d = str(day).zfill(2)
    
    # ダウンロード先のリンクを指定
    url = make_url(year, month, day)
    title =  str(year) + str_m + str_d + ".zip"
    print(url)
    try:
        # データを取ってくる
        urllib.request.urlretrieve(url,title)
         # Zipファイルを開く
        with zipfile.ZipFile(title) as existing_zip:
            existing_zip.extractall('data')
        # ZIpファイルは不要なので消す
        if os.path.isfile(title):
            os.remove(title)
    except urllib.error.HTTPError as e:
        raise e
    except urllib.error.URLError as e:
        raise e


# DEBUG
# year = 2019
# month = 9
# day = 11
# getCSVFile(year, month, day)


# In[9]:


def write_csv(data_list):
    other = [ 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Numeric', 'Category']
    headers = [ '3m', '5m', '10m','30m', '1h','2h', '3h', '5h', 'fav', 'retweet',  'category']
    try:
        filename = "abe_255-2000.csv"
        with open(filename, 'w', newline='') as f:
            wrtr = csv.writer(f, delimiter=',')
            wrtr.writerow(other)
            wrtr.writerow(headers)
            for data in data_list:
                wrtr.writerow(data)
            f.close()
    except OSError as e:
        print('ファイル処理でエラー発生'.format(e.args))

def write_mycsv(data_list):
    headers = ['date','fav', 'retweet', '0m', '3m', '5m', '10m','30m', '1h','2h', '3h', '5h',  'category']
    try:
        filename = "abe_255-3.csv"
        with open(filename, 'w', newline='') as f:
            wrtr = csv.writer(f, delimiter=',')
            wrtr.writerow(headers)
            for data in data_list:
                wrtr.writerow(data)
            f.close()
    except OSError as e:
        print('ファイル処理でエラー発生'.format(e.args))



# In[10]:


def is_exsisted_file(fileName):
    return os.path.exists(fileName)

# DEBUG
# trueName = "data/NSL_190701.csv"
# falseName = "data/NSL_190601.csv"
# print(is_exsisted_file(trueName))
# print(is_exsisted_file(falseName))


# In[11]:


# X分後の時間を入れたリストを作成する関数
# もし取引時間外だった場合は-1を返す
def check_datetime(t_time):
    tori_data = []
    tori_data.append(tori_time.check_toritime(t_time, 3))
    tori_data.append(tori_time.check_toritime(t_time, 5))
    tori_data.append(tori_time.check_toritime(t_time, 10))
    tori_data.append(tori_time.check_toritime(t_time, 30))
    tori_data.append(tori_time.check_toritime(t_time, 60))
    tori_data.append(tori_time.check_toritime(t_time, 120))
    tori_data.append(tori_time.check_toritime(t_time, 180))
    tori_data.append(tori_time.check_toritime(t_time, 300))
    
    return_data = []
    flag = False
    
    for h, m in tori_data:
        if h < 0:
            return_data.append("-1")
            flag = True
        elif flag:
            return_data.append("-1")
        else :
            m_2d = str(m).zfill(2)
            return_data.append('{}:{}'.format(h, m_2d))
#     print(return_data)
    return return_data

# DEBUG
#check_datetime(tori_time.encode(5,0))


# In[12]:


def make_fileName(year, month, day):
    str_m = str(month).zfill(2)
    str_d = str(day).zfill(2)
    return "data/NSL_" + str(year)[2:4] + str_m + str_d +".csv"


# In[13]:


def make_data(year, month, day,  t_time, str_time):
    # CSVのファイル名作成
    csvName = make_fileName(year, month, day)
    # ファイルの存在確認
    if  not(is_exsisted_file(csvName)):
        print("get file:"+csvName)
        #return []
        # １度動かしたらgetしているはずなので、コメントアウト
        try:
            getCSVFile(year, month, day)
        except urllib.error.HTTPError as e:
            return []
        except urllib.error.URLError as e:
            return []

    # CSVを開いてデータをいじる
    csv_file = open(csvName, "r", encoding="shift_jis", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    # csvにheaderが2つあるのでその分を飛ばす
    next(f)
    next(f)
    print("--------------")
    print(str_time)
    time_data = check_datetime(t_time)    
    print(time_data)
    ave = 0
    
    data_225 = [0, 0, 0,0,0,0,0,0,0]
    for row in f:
        if str_time == row[1]:
            ave = (int(row[3]) + int(row[4]))/2
            data_225[0] = ave
        # time_data ... データ数８個
        for i in range(len(time_data)):
            if time_data[i] == row[1]:
                if ave == 0:
                    return []
                n_ave = (int(row[3]) + int(row[4]))/2
                data_225[i + 1] = n_ave - ave
    
    # データサイズが足りない時はPCP表示でエラーが出るので0で埋める(ごめんなさい)
#     for d in time_data:
#         if d == "-1":
#             data_225.append(0)
            
    print(data_225)
            
    return data_225[1:]

#make_data(2019, 11, 26,  tori_time.encode(4, 0), "4:00")


# In[14]:


filename = "abe_tweet2000.csv"

csv_file = open(filename, "r", encoding="utf-8", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
print(f)
# csvにheaderがある場合
header = next(f)
print(header)
data_list = []
for row in f:
    data = []
    #print(row)
#     data.append('{}{}{}{}{}'.format(row[0], row[1], row[2], row[3],row[4]))
    
    data225 = make_data(row[0], row[1], row[2], row[5], row[6])
    if data225 == []:
        continue
    data = data + data225
    print(len(data))
    
    data_list.append(data)
    
    data.append(row[8])
    data.append(row[7])
    data.append(row[9])


write_csv(data_list)
# write_mycsv(data_list)


