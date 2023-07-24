#introduction to lists
guestlist = ["2Pac","Jason", "MJ", "Mike Tyson","Tyler"]

print(len(guestlist))

#invite each guest to the cookout
for i in guestlist:
    print("you are invited to the cook out " + i+"\n")

#now changing the guestlist
cantmakeit = guestlist[0]

print(cantmakeit + " cannot make it to the cookout anymore")
#3.5
guestlist[0] = "Jonston"
print("\n This is the new guest list below \n")
for i in guestlist:
    print("you are now invited invited to the cook out " + i+"\n")

#3.6
for i in guestlist:
    print("hi " + i+" we found a bigger table")

guestlist.insert(0,"Tommy")
guestlist.insert(3,"Mamoa")
guestlist.append("batman")
print("\n")
#print final guestlist
for i in guestlist:
    print("you are invited to the cook out " + i+"\n")
print("\n \n")

#3.7
print(len(guestlist))
#size = len(guestlist)-2

#for guests in guestlist:
#    remove_last = guestlist.pop()
#    print("Sorry dinner table isnt big enough " + remove_last)
#    print(len(guestlist))
#    if len(guestlist) == 2:
#        break
print("the number of guest is "+len(guestlist))

remove_last = guestlist.pop()
print("Sorry dinner table isnt big enough " + remove_last)

remove_last = guestlist.pop()
print("Sorry dinner table isnt big enough " + remove_last)

remove_last = guestlist.pop()
print("Sorry dinner table isnt big enough " + remove_last)

remove_last = guestlist.pop()
print("Sorry dinner table isnt big enough " + remove_last)

remove_last = guestlist.pop()
print("Sorry dinner table isnt big enough " + remove_last)

remove_last = guestlist.pop()
print("Sorry dinner table isnt big enough " + remove_last)

print(guestlist)
print("\n")

for i in guestlist:
    print("you are still invited to the cookout even though the table is smaller " + i +"\n")

guestlist.pop()
guestlist.pop()

print(len(guestlist))