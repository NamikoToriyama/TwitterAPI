
# coding: utf-8

# In[39]:


import numpy as np
import matplotlib.pyplot as plt
import csv
from pylab import rcParams
import matplotlib.pyplot as plt
import statistics
import math


# In[75]:


csv_file = open("./abe_255-2000.csv", "r", encoding="utf-8", errors="", newline="" )
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
# csvにheaderが2つあるのでその分を飛ばす
next(f)
header = next(f)
#print("--------------")

print(header[3:])
data = [[],[],[],[],[],[],[],[]]

data0 = [[],[],[],[],[],[],[],[]]
data2 = [[],[],[],[],[],[],[],[]]
data3 = [[],[],[],[],[],[],[],[]]

rn = 10

for row in f:
    #print(type(row[11]))
    for i in range(len(data0)):
            data[i].append(float(row[i]))
    if row[rn] == "0":
        for i in range(len(data0)):
            #print(row)
            data0[i].append(float(row[i]))
    elif row[rn] == "2":
        for i in range(len(data2)):
            data2[i].append(float(row[i]))
    elif row[rn] == "3":
        for i in range(len(data3)):
            data3[i].append(float(row[i]))


# print(data0)
print(len(data))
ave_data = []
ave_data0 = []
ave_data2 = []
ave_data3 = []

ave_data.append(0.)
ave_data0.append(0.)
ave_data2.append(0.)
ave_data3.append(0.)

for i in range(len(data)):
    ave_data.append(sum(data[i])/len(data[i]))
    ave_data0.append(sum(data0[i])/len(data0[i]))
    ave_data2.append(sum(data2[i])/len(data2[i]))
    ave_data3.append(sum(data3[i])/len(data3[i]))

print(ave_data)
print(ave_data0)
print(ave_data2)
print(ave_data3)



    


# In[96]:


x =  np.arange(0, 9, 1)
plt.plot(x, ave_data, color=(0,1,1))
# 一次関数をplot
y = 0*x
plt.plot(x, y, color=(0,0,0))

# 軸の設定
ydata =  np.arange(-5, 20, 5)
#plt.yticks(ydata)
plt.xticks([0,1, 2,3, 4, 5, 6, 7, 8], ['0m', '3m', '5m', '10m', '30m', '1h', '2h', '3h', '5h'])
rcParams['figure.figsize'] = 10,7
plt.show() # 描画


# In[92]:


x =  np.arange(0, 9, 1)
plt.plot(x, ave_data0, color=(1,0,0))
# 一次関数をplot
y = 0*x
plt.plot(x, y, color=(0,0,0))

# 軸の設定
ydata =  np.arange(-5, 20, 5)
plt.xticks([0,1, 2,3, 4, 5, 6, 7, 8], ['0m', '3m', '5m', '10m', '30m', '1h', '2h', '3h', '5h'])
rcParams['figure.figsize'] = 10,7
plt.show() # 描画


# In[84]:


x =  np.arange(0, 9, 1)
plt.plot(x, ave_data2, color=(0,1,0))
# 一次関数をplot
y = 0*x
plt.plot(x, y, color=(0,0,0))

# 軸の設定
ydata =  np.arange(-5, 20, 5)
plt.xticks([0,1, 2,3, 4, 5, 6, 7, 8], ['0m', '3m', '5m', '10m', '30m', '1h', '2h', '3h', '5h'])
rcParams['figure.figsize'] = 10,7
plt.show() # 描画


# In[83]:


x =  np.arange(0, 9, 1)
plt.plot(x, ave_data3, color=(0,0,1))
# 一次関数をplot
y = 0*x
plt.plot(x, y, color=(0,0,0))

# 軸の設定
plt.xticks([0,1, 2,3, 4, 5, 6, 7, 8], ['0m', '3m', '5m', '10m', '30m', '1h', '2h', '3h', '5h'])
rcParams['figure.figsize'] = 10,7
plt.show() # 描画


# In[87]:


x =  np.arange(0, 9, 1)
plt.plot(x, ave_data, color=(0.5,0.5,0.5))
plt.plot(x, ave_data0, color=(1,0,0))
plt.plot(x, ave_data2, color=(0,1,0))
plt.plot(x, ave_data3, color=(0,0,1))
# 一次関数をplot
y = 0*x
plt.plot(x, y, color=(0,0,0))

# 軸の設定
plt.xticks([0,1, 2,3, 4, 5, 6, 7, 8], ['0m', '3m', '5m', '10m', '30m', '1h', '2h', '3h', '5h'])
rcParams['figure.figsize'] = 10,7
plt.show() # 描画

