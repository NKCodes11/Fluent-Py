#1 to 20
one20 = list(range(1,21))
print(one20)

#1 to 1 million
#onemil = list(range(1,1000001))
#print(onemil)

#print(sum(onemil))
#print(min(onemil))
#print(max(onemil))

odd = list(range(1,21,3))
print(odd)

#threes
print("\n")
three = list(range(3,31,3))
print(three)

#cubes
cubes = []
for value in range(1,11):
    cubes.append(value**3)

print(cubes)

cube2 = [value**3 for value in range(1,11)]
print(cube2)