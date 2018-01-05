#-*-coding:utf-8-*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

"""
降维：
  1. PCA
  2. SVD
"""
"""
SVD 
"""
from sklearn.random_projection import sparse_random_matrix
from sklearn.decomposition import TruncatedSVD

X = np.random.randn(1000, 50)
svd = TruncatedSVD(n_components=5, n_iter=7, random_state=42)
svd.fit(X) 
svd.singular_values_
svd.explained_variance_ratio_



from numpy import *
U0, s0, V0 = linalg.svd(X)
V21 = dot(X.T, U0[:,:10])



from sklearn.utils.extmath import randomized_svd
U1, s1, V1 = randomized_svd(X, n_components=50)

U22, s22, V22 = randomized_svd(X, n_components=10)
