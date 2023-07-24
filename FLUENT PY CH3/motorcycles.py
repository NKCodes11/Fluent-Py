motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#identifying the index and giving it a namw will change what ever is at that indexed spot
motorcycles[0] = 'ducati'
print(motorcycles)
#append adds to the end of a list.
motorcycles.append("honda")

print(motorcycles)

#insert adds to the which ever spot is identified
motorcycles.insert(2,"ferrari")
print(motorcycles)

#you can delete elements by using delete or pop. pop will delete the last one and del will delete which ever is index.
popmotor = motorcycles.pop()
del motorcycles[0]

print(popmotor)
print(motorcycles)
# you can also pop by position as well

