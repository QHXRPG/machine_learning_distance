import numpy as np
import math
"""
1.欧几里得距离
2.曼哈顿距离/街区距离
3.闵可夫斯基距离 欧几里得距离(p=2)和曼哈顿距离(p=1)是闵可夫斯基距离的一种特殊情况
4.切比雪夫距离 二点之间的距离定义是其各坐标数值差绝对值的最大值
5.标准化的欧几里得距离 将各个分量都标准化到均值、反差相等的区间
6.汉明距离  表示两个字符串对应位不同的数量
7.余弦距离,用来衡量两个方向方向的差异，与向量幅度无关
"""
#%% 欧几里得距离
def Euclidean_distance(x,y):
    x = np.array(x)
    y = np.array(y)
    euclidean_distance = np.sqrt(np.sum(np.square(x-y)))
    return euclidean_distance

#%% 曼哈顿距离/街区距离
def Manhattan_distance(x,y):
    x = np.array(x)
    y = np.array(y)
    manhattan_distance = np.sum(np.abs(x-y))
    return manhattan_distance

#%% 闵可夫斯基距离 欧几里得距离(p=2)和曼哈顿距离(p=1)是闵可夫斯基距离的一种特殊情况
def Minkowski_distance(x,y,p):
    x = np.array(x)
    y = np.array(y)
    zipped = zip(x,y)
    minkowski_distance = math.pow(np.sum([math.pow(np.abs(i[0]-i[1]),p) for i in zipped]),1/p)
    return minkowski_distance,c

#%% 切比雪夫距离 二点之间的距离定义是其各坐标数值差绝对值的最大值
def Chebyshev_distance(x,y):
    x = np.array(x)
    y = np.array(y)
    chebyshev_distance = np.max(np.abs(x-y))

#%% 标准化的欧几里得距离 将各个分量都标准化到均值、反差相等的区间
def Standardized_Euclidean_distance(x,y):
    x = np.array(x)
    y = np.array(y)
    X = np.vstack([x,y])
    var = np.var(X, axis=0, ddof=1)
    standardized_Euclidean_distance = np.sqrt(np.sum(np.square(x-y)/var))
    return standardized_Euclidean_distance

#%% 汉明距离  表示两个字符串对应位不同的数量
def Hanming_distance(x,y):
    hanming_distance = sum(x_i != y_i for x_i, y_i in zip(x,y))
    return hanming_distance

#%% 余弦距离,用来衡量两个方向方向的差异，与向量幅度无关
def Cosine_distance(x,y):
    x = np.array(x)
    y = np.array(y)
    xy = np.dot(x,y)
    abs_xy = np.sqrt(np.sum(np.square(x))) * np.sqrt(np.sum(np.square(y)))
    cosine_distance = xy/abs_xy
    return cosine_distance