##################### 資料視覺化 (Matplotlib , Sraborn , Plotly) ########################

import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()
x = pd.DataFrame(iris["data"] , columns=iris["feature_names"])
# print("target name: "+ str(iris["target_names"]))
y = pd.DataFrame(iris["target"] , columns= ["target"])
data = pd.concat([x , y] , axis=1)
# print(data.head(3))


# # plt.plot([1,2,3,4]) #只有y軸的資料，x軸會自動產生0,1,2,3

# # plt.plot([1,2,3,4] , [1,4,9,16]) # x軸的資料是[1,2,3,4]，y軸的資料是[1,4,9,16]
# plt.xlabel("x-axis") # x軸的標籤
# plt.ylabel("y-axis") # y軸的標籤
# plt.title("Line Plot") # 圖表的標題


# plt.plot([1,2,3,4] , [1,4,9,16] , "ro") # "ro" 是指定線條的樣式，r是紅色，o是圓點

# plt.axis([0,6,0,20]) # axis 是指定x軸和y軸的範圍，前兩個數字是x軸的範圍，後兩個數字是y軸的範圍

# # plt.show()


# t = np.arange(0. , 5. , 0.2) # arange 是產生等差數列，第一個數字是起始值，第二個數字是終止值，第三個數字是步長
# # print("t:"+ str(t))


# # r-- 是紅色的虛線，bs是藍色的方形，g^是綠色的三角形
# plt.plot(t,t,"r--" ,t ,t**2 , "bs" , t , t**3 , "g^") 
# plt.xlabel("x-axis") # x軸的標籤
# plt.ylabel("y-axis") # y軸的標籤
# plt.title("Line Plot") # 圖表的標題
# # plt.show()


# x = [4,7,7,8,9,10,10,10,11,12,13,14,15,16,17,18,19,20]
# y = [2,10,4,22,16,10,23,21,16,23,21,16,23,21,16,23,21,16]
# plt.bar(x,y) # bar 是柱狀圖，x是x軸的資料，y是y軸的資料
# # plt.show()

# x = [4,7,7,8,9,10,10,10,11,12,13,14,15,16,17,18,19,20]
# y = [2,10,4,22,16,10,23,21,16,23,21,16,23,21,16,23,21,16]
# plt.scatter(x,y) # scatter 是散點圖，x是x軸的資料，y是y軸的資料
# # plt.show()



##################### Pandas plot ########################

print(data.head(3))

# scatter 是散點圖，x是x軸的資料，y是y軸的資料，c是顏色
# data.plot.scatter(x = "sepal length (cm)" , y = "sepal width (cm)" , c = "target" ) 

color = {
    0:"r",
    1:"g",
    2:"b"
}
data["target"] = data["target"].map(color)
# print(data.head(3))
# data.plot.scatter(x = "sepal length (cm)" , y = "sepal width (cm)" , c = "target" )

# plt.show()

# # data[data["target"]=="r"].plot.scatter(x = "sepal length (cm)" , y = "sepal width (cm)" , c = "r" , label="setosa")
# # data[data["target"]=="g"].plot.scatter(x = "sepal length (cm)" , y = "sepal width (cm)" , c = "g" , label="versicolor")
# # data[data["target"]=="b"].plot.scatter(x = "sepal length (cm)" , y = "sepal width (cm)" , c = "b" , label="virginica")


# ax = data[data["target"]=="r"].plot.scatter(x = "sepal length (cm)" , y = "sepal width (cm)" , c = "r" , label="setosa" , alpha = 0.5)
# ax = data[data["target"]=="g"].plot.scatter(x = "sepal length (cm)" , y = "sepal width (cm)" , c = "g" , label="versicolor" , ax = ax , alpha = 0.5)
# data[data["target"]=="b"].plot.scatter(x = "sepal length (cm)" , y = "sepal width (cm)" , c = "b" , label="virginica" , ax = ax , alpha = 0.5) 

# plt.show()


# n = 50
# x = np.random.rand(n) # 隨機產生0~1之間的數字，產生n個數字
# y = np.random.rand(n) # 隨機產生0~1之間的數字，產生n個數字
# color = np.random.rand(n)
# area = np.pi*(15*np.random.rand(n))**2 #隨機產生0~15之間的數字，然後平方，最後乘以pi，得到圓的面積

# plt.scatter(x , y , s = area , c = color , alpha = 0.5) # alpha 是透明度，0.5是半透明
# plt.show()


# plt.style.available # available 是可用的樣式，這裡是列出所有可用的樣式
# plt.style.use("ggplot") # ggplot 是一種樣式，這裡是使用ggplot樣式
# plt.scatter(x , y , s = area , c = color , alpha = 0.5)
# plt.show()


# plt.style.use("classic") # classic 是一種樣式，這裡是使用classic樣式
# plt.scatter(x , y , s = area , c = color , alpha = 0.5)
# plt.show()


##################### Seaborn ########################
import seaborn as sns

d = {
    "r":0,
    "g":1,
    "b":2
}

# target_name = {
#     0:"setosa",
#     1:"versicolor",
#     2:"virginica"
# }

data["target"] = data["target"].map(d)
print(data.head(3))

# plt.style.use("ggplot") # ggplot 是一種樣式，這裡是使用ggplot樣式
# sns.lmplot(x = "sepal length (cm)" , y = "petal width (cm)" , data = data , fit_reg = False , hue = "target" ) 
# plt.show()
# data["target_name"] = data["target"].map(target_name)





# # fit_reg 是是否顯示回歸線，hue 是根據哪一個欄位來區分顏色
# sns.lmplot(x = "sepal length (cm)" , y = "petal width (cm)" , data = data , fit_reg = False , hue = "target_name" ) 
# plt.show()


##################### Plotly ########################


import plotly.graph_objects as go
# import plotly.plotly as py

# fig = go.Figure(
#     data = [go.Scatter(x = [1,2,3,4] , y = [1,2,3,4])],
#     layout = go.Layout(title = "Line Plot")
# )
# fig.show()

n = 1000
r_x = np.random.rand(n)
r_y = np.random.rand(n)

# trace = go.Scatter(
#     x = r_x,
#     y = r_y,
#     mode = "markers",
# )

# test = [trace]

# # layout 是圖表的佈局，這裡是指定圖表的標題為Scatter Plot
# fig = go.Figure(data = test , layout = go.Layout(title = "Scatter Plot")) 
# fig.show()


trace0 = go.Scatter(
    x = data[data["target"]==0]["sepal length (cm)"],
    y = data[data["target"]==0]["petal width (cm)"],
    mode = "markers", # markers 是散點圖，lines 是線圖，markers+lines 是散點圖和線圖
    name = "setosa"
)

trace1 = go.Scatter(
    x = data[data["target"]==1]["sepal length (cm)"],
    y = data[data["target"]==1]["petal width (cm)"],
    mode = "markers",
    name = "versicolor"
)

trace2 = go.Scatter(
    x = data[data["target"]==2]["sepal length (cm)"],
    y = data[data["target"]==2]["petal width (cm)"],
    mode = "markers",
    name = "virginica"
)

test_1 = [trace0 , trace1 , trace2]
fig = go.Figure(data = test_1 , layout = go.Layout(title = "Scatter Plot"))
fig.show()

# multivariate_normal 是產生多變量常態分布的隨機數，第一個參數是平均值，第二個參數是協方差矩陣，第三個參數是產生的隨機數的個數，transpose 是轉置，將行列互換
x,y,z = np.random.multivariate_normal(np.array([0,0,0]) ,np.eye(3) , 400).transpose() 


trace_1 = go.Scatter3d(
    x = x,
    y = y,
    z = z,
    mode = "markers",
    marker = dict(
        size = 12,
        color = z, # 設置顏色為z軸的值，這裡是根據z軸的值來區分顏色
        colorscale = "Viridis", # 選擇顏色的樣式，這裡是使用Viridis樣式
        opacity = 0.8
    )
)


data_test = [trace_1]
layout = go.Layout(
    margin = dict(
        l = 0,
        r = 0,
        b = 0,
        t = 0
    )
)

fig = go.Figure(data = data_test , layout = layout)
fig.show()

