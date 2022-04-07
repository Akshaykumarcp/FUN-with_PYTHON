""" 
- Python uses dynamic typing which is also called as duck typing. 
- If an object implements a method you can use it, irrespective of the type. 
- This is different from statically typed languages, where the type of a construct need to be explicitly declared. 

- Polymorphism is the ability to use the same syntax for objects of different types:
 """

def summer(a, b):
    return a + b

print(summer(1, 1))
print(summer(["a", "b", "c"], ["d", "e"]))
print(summer("abra", "cadabra"))
""" 
2
['a', 'b', 'c', 'd', 'e']
abracadabra """

# Polymorphism example
class Instagram:
    
    def share_stories(self):
        print("share your stories on Instagram!!!")
    
class Facebook:
    
    def share_stories(self):
        print("share your stories on Facebook!!!")

def ShareStory(application):
    application.share_stories()   

insta = Instagram()
fb = Facebook()

ShareStory(insta)
# share your stories on Instagram!!!

ShareStory(fb)
# share your stories on Facebook!!!