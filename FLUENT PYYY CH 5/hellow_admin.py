username = ['Josh', 'John', 'Jo', 'Nasir', 'Xan']
#capitalize everything so it is in line with new users.
for name in username:
    name.capitalize()

#new users for account database
new_user = ['Jamaal','joHn','James','Amia']

#check new users if the name is available. if its not
# available the system will let the user know and prompt them
for user in new_user:
    if user.capitalize() in username:
        print(user +" username is not available")
        

