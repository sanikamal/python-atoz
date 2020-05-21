# Create Usernames
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    uname = name.lower().replace(' ','_')
    usernames.append(uname)

print(usernames)
