u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l = 'abcdefghijklmnopqrstuvwxyz'

s = []
x = input()
while x != 'end':
    s.append(x)
    x = input()

for i in range(len(s)):
    for ch in s[i]:
        if ch in u:
            ch = u[(u.find(ch)+13)%26 -1]
        elif ch in l:
            ch = u[(u.find(ch)+13)%26 -1]

for i in range(len(s)):
    print(s[i])
# A 0 Z 25
# O 15 -> (15+13)%26 = 2 -1  = B 1

# learn nihongo with king linlin ideal 19sep2023
# zasshi
# 
# saifu
# u t ta
# tsu i t ta a
# bukkuofu
# ははは
# へへへへ
# ふふふふ
# 
# ツイッター
# 車
# パソコン
# シャツ