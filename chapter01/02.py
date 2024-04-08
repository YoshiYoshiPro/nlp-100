s1 = "パトカー"
s2 = "タクシー"
# 二つの文字列から交互に文字を取り出して連結
result = ''.join(s1[i] + s2[i] for i in range(len(s1)))
# result = ''.join(s1[i] + s2[i] for i in range(len(s1)))でも可

print(result)
