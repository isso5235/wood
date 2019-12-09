import numpy as np

T = 1000    #記号列の長さ
N = 2       #出力状態数

Pi_1 = np.array( [1.0, 0.0] )   #初期分布
A_1  = np.array( [[0.2, 0.8], [0.8, 0.2]] ) #推移確率
B_1  = np.array( [[0.8, 0.2], [0.2, 0.8]] ) #出力確率

O = [ np.random.choice( [0,1], p = [0.2, 0.8] ) for i in range(T) ]   #出力記号列

P_lambda = 0

alpha = np.zeros((T, N))
C = np.zeros((T))   #スケーリング用

#初期値設定
alpha[0, :] = Pi_1[:] * B_1[:, O[0]]
C[0] = alpha[0, :].sum()
alpha[0, :] /= C[0]

#繰り返し
for t in range(T-1):
    alpha[t+1, :] = alpha[t, :].dot(A_1) * B_1[:, O[t+1]]
    C[t+1] = alpha[t+1, :].sum()
    alpha[t+1, :] /= C[t+1]

#P(lambda)を計算
P_lambda = -np.log(C).sum()

print(-P_lambda)