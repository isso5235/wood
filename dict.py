import re

strings = "1:a 3:c 4:d"  # 辞書にしたい文字列
splited = re.split(" +", strings)  # スペースで分割
lists = []

for char in splited:  # コロンで分割後リストに追加
    tmp = char.split(":")
    lists.append(tmp)

dict = {k: v for (k, v) in lists}  # 辞書作成
print(dict)
