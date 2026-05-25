#透過sklearn的datasets模組來載入iris資料集，並使用pandas來處理資料，最後將特徵與目標變數合併成一個DataFrame。

from sklearn import datasets
iris = datasets.load_iris()
# print(iris.keys())
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
# print(iris['DESCR'])
# print(iris['feature_names'])
# print(iris['data'])
# print(iris['target'])
# print(iris['target_names'])

import pandas as pd
a = pd.DataFrame(iris["data"] , columns=iris["feature_names"])
# print(a)
b = pd.DataFrame(iris["target"] , columns=["target"])
# print(b)
data = pd.concat([a,b] , axis=1) # axis=1 是水平拼接，axis=0 是垂直拼接
# print(data)
# print(dict(enumerate(iris["target_names"]))) # {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

b1 = pd.DataFrame(pd.Series(iris["target"]).map(dict(enumerate(iris["target_names"]))) , columns=["target_name"])
# print(b1)

last = pd.concat([a,b1] , axis=1)
print(last)