s = input()

if s[-1] == 's' or s[-1] == 'x' or s[-2:] == 'ch':
  s += 'es'
elif s[-1] == 'y' and (s[-2] not in 'aeiou'):
  s = s[:-1]
  s += 'ies'
else:
  s += 's'

print(s)