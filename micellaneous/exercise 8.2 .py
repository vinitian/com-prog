# Create a variable named `count_alpha` as a dict
# that has key as all English alphabets (upper and lower cases),
# and has all values as 0.

alphabets = 'abcdefghijklmnopqrstuwxyz'
alphabets += alphabets.upper()
count_alpha = {}
for c in alphabets:
    count_alpha[c] = 0
print(count_alpha)