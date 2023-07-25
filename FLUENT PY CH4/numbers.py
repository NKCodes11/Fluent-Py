for value in range(1,6):
    print(value)

numbers = list(range(1,11))
print(numbers)

#you can also use range to print even numbers too. the last number in the range function is the step
even = list(range(2,11,3))
print(even)


#numbers lets make a list of squres
squares =[]

for square in range(1,11):
    square = square**2
    squares.append(square)

print(squares)

#Or
square2 = []
for value in range(1,11):
    square = value**2
    square2.append(square)

print("\n \n")    
print(squares)    

#OR

square3 = []
for value in range(1,11):
    square3.append(value**2)

print("\n \n")    
print(squares) 

#now for comprehension
squares = [value**2 for value in range(1,11)]
print("\n \n")    
print(squares)