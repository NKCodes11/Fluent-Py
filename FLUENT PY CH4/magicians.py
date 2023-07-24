
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

'''
A Closer Look at Looping
The concept of looping is important because its one of the most common
ways a computer automates repetitive tasks. For example, in a simple loop
like we used in magicians.py, Python initially reads the first line of the loop:
for magician in magicians:
This line tells Python to retrieve the first value from the list magicians
and store it in the variable magician. This first value is alice. Python then
reads the next line:
print(magician)
Python prints the current value of magician, which is still alice. Because
the list contains more values, Python returns to the first line of the loop:
for magician in magicians:
Python retrieves the next name in the list, 'david', and stores that value
in magician. Python then executes the line:
print(magician)
Python prints the current value of magician again, which is now 'david'.
Python repeats the entire loop once more with the last value in the list,
carolina. Because no more values are in the list, Python moves on to the
next line in the program. In this case nothing comes after the for loop, so
the program simply ends.
When youre using loops for the first time, keep in mind that the set of
steps is repeated once for each item in the list, no matter how many items
are in the list. If you have a million items in your list, Python repeats these
steps a million times—and usually very quickly.
Also keep in mind when writing your own for loops that you can choose
any name you want for the temporary variable that holds each value in the
list. However, its helpful to choose a meaningful name that represents a
single item from the list. For example, heres a good way to start a for loop
for a list of cats, a list of dogs, and a general list of items:
'''

print("\n")
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")


magicians = ['alice', 'david', 'carolina']
print("\n")
print("\nThis is bad indentation below:")
#this is bad indentation
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    print("Thank you everyone, that was a great magic show!")

print("test")