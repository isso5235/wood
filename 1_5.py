import numpy as np
import random
import math
import matplotlib.pyplot as plt

#変数
P1, P2 = 0.5, 0.5   #クラスc1, c2の発生確率
r = 10              #パターンの属性数
pk = np.zeros(((2,2,r)))  #クラス内の各属性の確率（xk = 0）
N = 300              #識別するパターンの数
Pr = 0           #識別率の実験値
X = []
Y = []

for num in range(N):
    #prに値を入れる
    for i in range(r):
        #pk( 0 | c1)を求める
        pk[0,0,i] = random.random()
        #pk( 1 | c1)を求める
        pk[0,1,i] = 1 - pk[0,0,i]
        
        #pk( 0 | c2)を求める
        pk[1,0,i] = random.random()
        #pk( 1 | c2)を求める
        pk[1,1,i] = 1 - pk[1,0,i]


    #識別関数gのパラメータw0からwrを求める
    w = []
    w.append(math.log(P1/P2))

    for i in range(r):
        w[0] += (math.log(pk[0,0,i]/pk[1,0,i]))

    for i  in range(r):
        w.append((math.log( (pk[0,1,i]/pk[1,1,i])/(pk[0,0,i]/pk[1,0,i]) )))


    #識別のシュミレーション実験
    Nr = 0  #正しく識別されたパターン数

    for i in range(N):
        C = np.random.choice([0,1], p=[P1,P2]) #クラスCの分布
        if C == 0:
            x = [ np.random.choice( [0,1], p=[pk[0,0,j], pk[0,1,j]] ) for j in range(r) ]
        else:
            x = [ np.random.choice( [0,1], p=[pk[1,0,j], pk[1,1,j]] ) for j in range(r) ]

        g = 0
        g = w[0] 
        for k in range(r):
            g += w[k+1] * x[k]

        if (C == 0 and g >= 0) or (C == 1 and g < 0):
            Nr += 1

    #識別率の実験値を求める
    Y.append(Nr/N)
    X.append(num + 1)

plt.plot(X, Y)
plt.ylim(0, 1)
plt.show()