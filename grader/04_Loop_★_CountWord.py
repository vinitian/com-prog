# Counting Keywords

count = 0
kw = input()
s = input()
words = s.replace('.',' ').split(' ') # replace the punctuations with whitespace, then split by whitespace

# print(words)

for i in range(len(words)):
    words[i] = words[i].strip('\'\".,()')

# print(words)

for i in range(len(words)):
    if words[i] == kw:
        count += 1
        
print(count)