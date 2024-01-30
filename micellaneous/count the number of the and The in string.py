# count the number of 'the' and 'The'
# comProg slide 4

s = input()
s2 = ''
for ch in s:
    if ch not in '/\'\",.()':
        s2 += ch

print(s3)

count = 0
for i in range(len(s3)):
    if s3[i] == 'the' or s3[i] == 'The':
        count += 1
        
print(count)
# The word "the" is one of the most common words in English.