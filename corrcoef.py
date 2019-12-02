
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import csv
from pylab import rcParams
import matplotlib.pyplot as plt
import statistics
import math


# In[4]:


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
print(len(data[0]))

print(len(data0[0]))
print(len(data2[0]))
print(len(data3[0]))


# In[5]:


print(np.corrcoef(data[0], data[1:]))

# print(np.corrcoef(data0[0], data0[1:]))
# print(np.corrcoef(data2[0], data2[1:]))
# print(np.corrcoef(data3[0], data3[1:]))


# In[8]:


# 相関係数を可視化
x =  np.arange(0, 8, 1)
# # 一次関数をplot
# y = 0*x
# plt.plot(x, y, color=(1,0,0))
all_c = [ 1. ,   0.85636582,  0.66891765,  0.3652304,   0.42563506,  0.10650342, -0.1291547,  -0.03228344]
o_c = [ 1. ,        0.90150832,  0.77458329,  0.43638665,  0.58862995,  0.09049361, -0.30024194, -0.09218312]
d_c = [ 1.  ,        0.67779394 , 0.2883002  , 0.19383088,  0.00192 ,    0.03783418, -0.01107374, -0.06301552]
p_c = [1.  ,       0.81212303 ,0.5117608 , 0.25567963, 0.27290183, 0.22786498, 0.21786213, 0.1714625 ]


plt.plot(x, all_c, color=(0.5,0.5,0.5))
plt.plot(x, o_c, color=(1,0,0))
plt.plot(x, d_c, color=(0,1,0))
plt.plot(x, p_c, color=(0,0,1))
y = 0*x
plt.plot(x, y, color=(0,0,0))


# 軸の設定
ydata =  np.arange(-0.4, 1.1, 0.1)
plt.yticks(ydata)
plt.xticks([0, 1, 2,3, 4, 5, 6, 7, 8], [ '3m', '5m', '10m', '30m', '1h', '2h', '3h', '5h', '...'])

rcParams['figure.figsize'] = 10,7
plt.show() # 描画


# In[9]:


x =  np.arange(0, 8, 1)
# # 一次関数をplot
# y = 0*x
# plt.plot(x, y, color=(1,0,0))
all_c = [ 1.     ,     0.82337534,  0.65194291 , 0.38055128 , 0.36916442  ,0.21562603, 0.01535236  ,0.10390779]
o_c =[ 1.     ,     0.84179723,  0.72152449 , 0.37243329  ,0.45867633  ,0.19295808,  -0.01734786  ,0.12352826]
d_c = [ 1.  ,        0.65833158 , 0.33748495 , 0.25762128 ,-0.01854626 ,-0.00683466,   -0.0706354,  -0.03665038]
p_c =[1.   ,      0.83685555, 0.59604192, 0.44623809, 0.38055563, 0.37351109,   0.13315192, 0.27525254]


plt.plot(x, all_c, color=(0.5,0.5,0.5))
plt.plot(x, o_c, color=(1,0,0))
plt.plot(x, d_c, color=(0,1,0))
plt.plot(x, p_c, color=(0,0,1))
y = 0*x
plt.plot(x, y, color=(0,0,0))


# 軸の設定
ydata =  np.arange(-0.4, 1.1, 0.1)
plt.yticks(ydata)
plt.xticks([0, 1, 2,3, 4, 5, 6, 7, 8], [ '3m', '5m', '10m', '30m', '1h', '2h', '3h', '5h', '...'])

rcParams['figure.figsize'] = 10,7
plt.show() # 描画

