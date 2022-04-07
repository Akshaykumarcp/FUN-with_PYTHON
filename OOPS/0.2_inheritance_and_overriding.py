""" 
- Through inheritance one can take all the methods and attributes from the another class and we can override or extend 
        the methods from the another class. 
- The class which is overriding is called child class and the class from methods are taking is called parent class. """

# PARENT CLASS
class Person:

    # class attribute
    skin_color = "white"

    # self can also be referred as a
    def __init__(a, name, surname, year_of_birth):
        a.name = name # attribute
        a.surname = surname
        a.year_of_birth = year_of_birth
    
    # method
    def age(a, current_year):
        return current_year - a.year_of_birth
    
    def __str__(a):
        return "%s %s was born in %d ." % (a.name, a.surname, a.year_of_birth)
    
# CHILD CLASS
class Student(Person): # inheritance

    def __init__(self, student_id, *args):
        super(Student, self).__init__(*args)
        self._student_id = student_id
        
ak = Student(1, 'akshay', 'kumar', 2006)

print(ak._student_id)
print(type(ak))
print(isinstance(ak, Person))
print(isinstance(ak, object))
""" 
1
<class '__main__.Student'>
True
True """

""" 
Overriding methods
- Inheritance allows to add new methods to a subclass but often is useful to change the behavior of a method defined 
        in the superclass. To override a method, define method again.
"""

class Student(Person):
    def __init__(self, student_id, *args, **kwargs):
        super(Student, self).__init__(*args, **kwargs)
        self._student_id = student_id
        
    def __str__(self): # overiding parent class method
        return super(Student, self).__str__() + " And has ID: %d" % self._student_id
        
ak = Student(1, 'akshay', 'kumar', 2006)
print(ak)
# akshay kumar was born in 2006 . And has ID: 1