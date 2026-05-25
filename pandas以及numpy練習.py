from sklearn import datasets
import pandas as pd
import numpy as np
iris = datasets.load_iris()
# print(iris["feature_names"])
x = pd.DataFrame(iris["data"] , columns=iris["feature_names"])
# print(x)
y = pd.DataFrame(iris["target"] , columns= ["target"])
# print(y)
data = pd.concat([x , y] , axis=1)
# print(data.head(3))

# list1 = [1,2,3,4,5]
# print(np.array(list1))


# list2 = ["1" , 2 , 3. , 4 , 5]
# print(np.array(list2))


##################### Pandas Series 表格裡面的一個column或一個欄位########################
s1 = pd.Series([1,45,78, np.nan , 100])
# print(type(s1))
# print(s1)

s2 = pd.Series([1,2,3] ,index=["a","b","c"])
# print(type(s2))
# print(s2)
# print(s2[0])


# print(type(data["sepal length (cm)"].head(5)))
# print(data["sepal length (cm)"].head(5))
# print(data[["sepal length (cm)"]].head(5))
# print(type(data[["sepal length (cm)"]].head(5)))



##################### Pandas DataFrame ########################

# print(np.random.randn(6,4))


df = pd.DataFrame(np.random.randn(6,4) , columns=["A","B","C","D"])
# print(df)


# print(data.info())
# print(data.describe())
# print(data.columns)

# print(data.sort_values(by="sepal length (cm)") .head(5)) # sort_values 是排序，by是依據哪一個欄位，ascending是升冪還是降冪


##################### Data Selection ########################

# print(data["sepal length (cm)"].head(5)) 
# print(data["sepal length (cm)"][2:5])
# print(data[2:5]["sepal length (cm)"])
# print(data[["sepal length (cm)" , "sepal width (cm)"]].head(5))

# print(data[["sepal length (cm)" , "sepal width (cm)"]][5:10])
# print(data.loc[5:10 , ["sepal length (cm)" , "sepal width (cm)"]]) # loc 是根據標籤來選取資料，iloc是根據位置來選取資料


##################### Data Selection with condition 資料篩選 ########################


# print(data[data["sepal length (cm)"]>7])


# print(data[data["target"].isin([1,2])]) # isin 是判斷某個欄位的值(範例為1~2)是否在某個列表裡面，返回一個布林值的Series




##################### Data Calculation 資料運算 ########################

# print(data.head(5))
# print(data.add(1))
# print(data.apply(lambda x : x+1).head(5))
# print(data["sepal length (cm)"].apply(lambda x : x+2)[:3])
# print(data["sepal length (cm)"].map(lambda x : x+2).head(5))
# print(data.map(lambda x : x+2).head(5)) # map 是對整個DataFrame的每一個元素都進行運算，apply是對整個DataFrame的每一列或每一行進行運算，applymap是對整個DataFrame的每一個元素進行運算



##################### Data Grouping 資料分群 ########################

print(data.head())
# print(data.groupby(by = "target").sum()) # groupby 是根據某個欄位的值(範例為target)來分組，sum是對每個組別的數值欄位進行加總，還有mean是平均值，count是計數，max是最大值，min是最小值

# print(data.groupby(by = "target").mean())

# for i in data.groupby(by="target"):
#     print(i)

df = data.groupby(by = "target").apply(lambda x : x.sort_values(by = ["sepal length (cm)"] , ascending=False)[1:2])
# groupby 是根據某個欄位的值(範例為target)來分組，apply是對每個組別的數值欄位進行運算，lambda x : x.sort_values(by = ["sepal length (cm)"] , ascending=False)[1:2] 是對每個組別的數值欄位進行排序，並且取出排序後的第2筆資料(索引為1)，這裡是取出每個組別的sepal length (cm)排序後的第2筆資料
# print(df)

df1 = data[data["target"]==0]["sepal length (cm)"].sort_values(ascending=False)
print(df1)










