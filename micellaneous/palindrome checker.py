s = input()

for i in range(len(s)//2):
    if s[i] != s[-i-1]:
        print('Not a palindrome')
        break
    if i == len(s)//2 -1:
        print('Hell yeah palindrome!!')