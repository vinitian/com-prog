d, m, y = input().split("/")

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

m = int(m)

print(month[m-1] + " " + d + ", " + y)