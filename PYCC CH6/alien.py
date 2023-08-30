alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']

print("you jsut earned " + str(new_points) + " points!")

#you can add to dictionary easily by just calling the dictionary and adding the variable
#just a note python does not care about the order in which they are added. its a dictionary so that makes sense
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25

print("\n this is the new alien_o dictionary with key pairs below:\n")
print(alien_0)

