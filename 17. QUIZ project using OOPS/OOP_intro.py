# class is a blueprint of real world object

# in this example, lets create a blueprint class for a website users

# for class name, follow PascalCase convention
# class name should not follow camelCase or snake_case convention
class User:

    # specify object attribute info at the time of object creation using contructor
    def __init__(self,userid, username): # constructor
        self.id = userid 
        self.username = username
        self.followers = 0 # provide default value
        self.following = 0

    def follow(self,user): # object method
        user.followers += 1
        self.following +=1

user_1 = User("1","ak") # object creation
user_2 = User("2","kumar")

""" 
user_1.id = "001"
user_1.username = "akshay"
"""

print(user_1)
# <__main__.User object at 0x000001DF416B4088>

# using object attributes
print(user_1.id)
print(user_1.username)
print(user_1.followers)
# 1
# ak
# 0

# using object method
user_1.follow(user_2)
print(user_1.followers) # 0
print(user_1.following) # 1
print(user_2.followers) # 1
print(user_2.following) # 0


