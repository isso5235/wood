import numpy as np
import math

#変数
P1, P2 = 0.5, 0.5   #クラスc1, c2の発生確率
r = 2              #パターンの属性数
m1, m2 = np.array([[-2], [-1]]), np.array([[1], [3]])  #クラス内の平均ベクトル
S = np.array([[1.5, 0.5],[0.5, 2.5]])   #共分散行列
N = 100              #識別するパターンの数
Pr = 0           #識別率の実験値

#識別関数gのパラメータw0からwrを求める
w = math.log(P1/P2)
w += np.dot(-(m1 + m2).T/2, np.linalg.inv(S))
w = np.dot(w, (m1 - m2))
wt = np.dot(np.linalg.inv(S), (m1 - m2))

#識別のシュミレーション実験
Nr = 0  #正しく識別されたパターン数

for i in range(N):
    C = np.random.choice([0,1], p=[P1,P2])

    if C == 0:
        x = np.random.multivariate_normal([m1[0,0],m1[1,0]], S, 1)
    else:
        x = np.random.multivariate_normal([m2[0,0],m2[1,0]], S, 1)

    g = 0
    g = w + np.dot(x, wt)

    if (C == 0 and g >= 0) or (C == 1 and g < 0):
        Nr += 1

#識別率の実験値を求める
print(Nr/N)
