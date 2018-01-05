#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
消除量纲
目的：避免数据由于不同量纲问题导致的对结果产生较为倾斜的影响
方法：
  1. 归一化
     范围： 0~1 之间
     方法： 线性变化 —— (x - min) / (max - min)
            对数切换 —— log10(x)
            反余切函数转换 —— atan(x) * 2 / pi
     目的： 消除不同数据的量纲，有量纲 ——> 无量纲， 无量纲 ——> 纯量。可以提高模型收敛速度和精度。
  2. 标准化
     范围： -1~1 之间
     方法： z-score 标准化 —— (x - mu) / sigma
            小数定标标准化 —— x / 10 ^ j (max(|j|) < 1)
            对数logistic   —— 1 / (1 + e ^ (-x))
            模糊量化数据   —— 1/2 + 1/2 * sin(pi / (max - min) * (X - (max - min) / 2))
     目的： 数据缩放，适用于符合标准正态分布的数据。方便不同量级的特征的加权和分析
  3. 正则化
     范围： 0~1 之间
     方法： L1正则化 —— 降低参数的绝对值相加（存在显著作用的少数的主要特征）x / sum(|x|)
            L2正则化 —— 对各参数的平方和再求平方根（特征作用相对平均）x / sum(x ^ 2) ^ (1/2)
     目的： 将样本缩放到单位范数内，主要针对稀疏的数据，防止模型参数的泛化
"""
from sklearn import preprocessing as pp
def standard(df_new, df, user_list):
    X = df_new.values.astype(float)
    #标准化
    X_scaled = pp.scale(X)
    X_scaler = pp.StandardScaler().fit_transform(X)
    #正则化
    X_norm = pp.normalize(X)
    X_norma = pp.Normalizer().fit_transform(X)
    #归一化
    X_std = pp.MinMaxScaler().fittransform(X)
    return pd.concat([pd.DataFrame(X_scaled, index = df_new.index, columns = list(df_new.columns)), df[user_list]], axis = 1)