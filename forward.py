import numpy as np
import math
from decimal import *

getcontext().prec = 100

T = 1000    #記号列の長さ
N = 2       #出力状態数

Pi_1 = np.array( [1.0, 0.0] )   #初期分布
A_1  = np.array( [[0.2, 0.8], [0.8, 0.2]] ) #推移確率
B_1  = np.array( [[0.8, 0.2], [0.2, 0.8]] ) #出力確率

O_1 = [ np.random.choice( [0,1], p = [0.2, 0.8] ) for i in range(T) ]   #出力記号列
O_2 = [ np.random.choice( [0,1], p = [0.2, 0.8] ) for i in range(T) ]   #出力記号列

P_lambda = 0

alpha = np.zeros((T, N))

#初期値設定
for j in range(N):
    alpha[0, j] = Pi_1[j] * B_1[j, O_1[0]]
    #print(alpha[0, j])

#繰り返し
for t in range(T-1):
    #print(B_1[j, O_1[t+1]])
    for j in range(N):
        Sum = 0
        for i in range(N):
            Sum += alpha[t, i] * A_1[i,j]
            print(math.log(Sum))
            #print(Decimal(alpha[t, i] * A_1[i,j]))
        alpha[t+1, j] = Sum*B_1[j, O_1[t+1]]   
        

#P(lambda)を計算
for j in range(N):
    P_lambda += alpha[T-1, j]


#print(np.log(P_lambda))

#np.dot(alpha[t-1, :], A)
