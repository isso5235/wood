import numpy as np

s_symbol = [ "w1", "w2", "w3" ] # 状態
c = len(s_symbol)               # 状態数
v_symbol = [ "v1", "v2" ]       # 出力記号
m = len(v_symbol)               # 出力数

# 遷移確率行列
A = np.array([[0.1, 0.7, 0.2], [0.2, 0.1, 0.7], [0.7, 0.2, 0.1]])
# 出力確率行列
B = np.array([[0.9, 0.1], [0.6, 0.4], [0.1, 0.9]])
# 初期確率行列
p = np.array([1/3, 1/3, 1/3])

class HMM:

    def __init__(self, p, A, B): 
        self.p = p
        self.A = A
        self.B = B

    def forward(self, x, c):
        n = len(x) # 観測回数

        # 前向きアルゴリズム
        alpha = np.zeros((n, c))

        # Step1
        alpha[0, :] = p[:] * B[:, x[0]]

        # Step2
        for t in range(1, n):
            alpha[t, :] = np.dot(alpha[t-1, :], A) * B[:, x[t]]
            print(alpha[t, :])

        # Step3
        return round(np.sum(alpha[-1]), 3)

    def backward(self, x, c):
        n = len(x) # 観測回数

        # 後ろ向きアルゴリズム
        # Step1
        beta = np.zeros((n, c))
        beta[-1, :] = 1

        # Step2
        for t in range((n-1), 0, -1):
            beta[t-1, :] = np.dot(self.A, (self.B[:, x[t]] * beta[t, :]))

        # Step3
        return round(sum(p[:] * self.B[:, x[0]] * beta[0, :]), 3)

if __name__=="__main__":
    # 観測結果
    x = [ 0, 1, 0 ] # v1, v2, v1という結果

    hmm = HMM(p, A, B)
    print(hmm.forward(x, c))
    #print(hmm.backward(x, c))