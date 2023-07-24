#introductiong to sorting lists lets work with car names
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse= True)
print(cars)

#Sort vs sorted function. 
#the sort will permanent change the list while sorted will only remporarily change the list

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("\n"+"Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#you can also print in reverse order which is the same as order but reversed
print("\n Here is the original list again: then reversed")
print(cars)
cars.reverse()
print(cars)

#len is another great function to use whici will give the length of a list.
'''
Youll find len() useful when you need to identify the number of aliens
that still need to be shot down in a game, determine the amount of data
you have to manage in a visualization, or figure out the number of registered users on a website, among other tasks.
'''
print("final")