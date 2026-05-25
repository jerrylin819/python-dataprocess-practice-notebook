import numpy as np
import pandas as pd
from sklearn import datasets
from io import StringIO
from IPython.display import Math

csv_data = '''
            A,B,C,D,E
            3.0,4.0,5.0,7.0,11
            2.0,,8.0,7.0,1.0
            1.0,2.0,3.0,4.0,5.0
            4.0,5.0,6.0,,9.0
            5.0,6.0,,8.0,
            '''

##################### Missing Data 空值資料處理 ########################
df = pd.read_csv(StringIO(csv_data))
# print(df)

# print(df.dropna()) # dropna 是刪除有缺失值的行，axis=0 是刪除行，axis=1 是刪除列
# print(df.dropna(how="all")) # how="all" 是刪除全部都是缺失值的行
# print(df.dropna(subset=["C"])) # subset 是指定要檢查哪一個欄位的缺失值
# print(df.fillna(0)) # fillna 是填補缺失值，0 是填補的值
df["B"] = df["B"].fillna(df["B"].mean()) # df["B"].mean() 是計算欄位B的平均值，然後用平均值來填補缺失值
df["C"] = df["C"].fillna(df["C"].mode()[0]) # df["C"].mode() 是計算欄位C的眾數，然後用眾數來填補缺失值
df["D"] = df["D"].fillna(df["D"].median()) # df["D"].median() 是計算欄位D的中位數，然後用中位數來填補缺失值
df["E"] = df["E"].fillna(df["E"].min()) # df["E"].min() 是計算欄位E的最小值，然後用最小值來填補缺失值
# print(df)


##################### Cetegorical Data 類別資料處理 ########################

df2 = pd.DataFrame(
    [["green" , "M" , 10.1 , 1],
     ["red" , "L" , 13.5 , 2],
     ["blue" , "XL" , 15.3 , 1]
    ]
)
df2.columns = ["color" , "size" , "price" , "classlabel"]
# print(df2)

size_mapping = {
    "XL" : 3,
    "L" : 2,
    "M" : 1
}
df2["size"] = df2["size"].map(size_mapping)
# print(df2)

pd.get_dummies(df2["color"]) # get_dummies 是將類別資料轉換成數值資料，這裡是將color欄位的類別資料轉換成數值資料，會產生三個新的欄位，分別是color_blue, color_green, color_red，對應到原本的color欄位的三個類別資料，當原本的color欄位的值是blue時，color_blue欄位的值為1，其他兩個欄位的值為0，以此類推


one_hot_encodding = pd.get_dummies(df2["color"] , dtype=int, prefix="color") # prefix 是指定新的欄位名稱的前綴詞，這裡是將color欄位的類別資料轉換成數值資料，會產生三個新的欄位，分別是color_blue, color_green, color_red

df2 = df2.drop("color" , axis=1)# drop 是刪除欄位，axis=0 是刪除行，axis=1 是刪除列

df2 = pd.concat([one_hot_encodding , df2] , axis=1) # axis=1 是水平拼接，axis=0 是垂直拼接
# print(df2)



##################### Normalization 資料正規化 ########################

Math(r"x^{(i)}_{norm} = \frac{x^{(i)} - x_{min}}{x_{max} - x_{min}}")


iris = datasets.load_iris()
x = pd.DataFrame(iris["data"] , columns=iris["feature_names"])
# print("target name: "+ str(iris["target_names"]))
y = pd.DataFrame(iris["target"] , columns= ["target"])
data = pd.concat([x , y] , axis=1)
print(data.head(3))


# 利用最小-最大正規化來將sepal length (cm)欄位的資料進行正規化，將資料縮放到0和1之間
data["sepal length (cm)"] = (data["sepal length (cm)"] - data["sepal length (cm)"].min()) / (data["sepal length (cm)"].max() - data["sepal length (cm)"].min()) 
print(data.head(3))



##################### Standardization 資料標準化 ########################


Math(r"x^{(i)}_{std} = \frac{x^{(i)} - \mu_{x}}{\sigma_x}")

data["sepal width (cm)"] = (data["sepal width (cm)"] - data["sepal width (cm)"].mean() )/(data["sepal width (cm)"].std())
print(data.head(3))













