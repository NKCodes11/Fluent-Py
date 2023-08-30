#for aliens 2 we start with an empty dictionary
alien_0 = {}

print(alien_0)

#usually we will use dictionary for user supplier data

#to modify data you just need to call the pair again and set it
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
alien_0['speed'] = 'medium'
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
alien_0['points'] = 25
print("Original x positon: "+ str(alien_0['x_pos']))


# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# The new position is the old position plus the increment. 
alien_0['x_position'] = alien_0['x_pos'] + x_increment

print("\nNew x-position: " + str(alien_0['x_pos']))

alien_0['speed'] = 'fast'

#you can remove key value pairs permanently by using the del command
del alien_0['points']


print(alien_0)

