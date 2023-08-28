numbers = [*range(1, 10, 1)]
print(numbers)

for ordN in numbers:
    if ordN == 1:
        print(str(ordN) +"st")
    elif ordN == 2:
        print(str(ordN) +"nd")
    elif ordN == 3:
        print(str(ordN) +"rd")
    else:
        print(str(ordN) +"th")