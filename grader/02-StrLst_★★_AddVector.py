vec1 = input()
vec2 = input()

# putting values in u
u = [0, 0, 0]

u[0] = vec1.split(", ")[0].split("[")[1]
u[1] = vec1.split(", ")[1]
u[2] = vec1.split(", ")[2].split("]")[0]

u[0] = float(u[0])
u[1] = float(u[1])
u[2] = float(u[2])

# putting values in v
v = [0, 0, 0]

v[0] = vec2.split(", ")[0].split("[")[1]
v[1] = vec2.split(", ")[1]
v[2] = vec2.split(", ")[2].split("]")[0]

v[0] = float(v[0])
v[1] = float(v[1])
v[2] = float(v[2])

#print(u[0], u[1], u[2])
#print(v[0], v[1], v[2])

#adding the vectors

sum = [u[0]+v[0], u[1]+v[1], u[2]+v[2]]

print('{0} + {1} = {2}'.format(u, v, sum))