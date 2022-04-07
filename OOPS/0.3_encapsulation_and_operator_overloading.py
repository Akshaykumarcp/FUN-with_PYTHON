""" 
- Encapsulation is powerful way to extend a class which consists on wrapping an object with a second one.
- Encapsulations is applications of a software or a program will not reveal the internal implementation details to the 
        outer world. 
- The only constraint on the programmer is to maintain the public interface for the component, as other programmers 
        will be writing code that depends on that developed interface. 
- Encapsulation allows the implementation details of a program to be change without affecting other parts of the program,
        thereby making it easier to fix bugs or add new functionality with some local changes to an application.

There are two main reasons to use encapsulation:
- Composition
- Dynamic Extension

Composition
- The abstraction process relies on creating a simplified model that remove useless details from a concept. 
- In order to be simplified, a model should be described in terms of other simpler concepts. 

- For example, we can say that a car is composed by:
    Tyres
    Engine
    Body
And break down each one of these elements in simpler parts until we reach primitive data. """

class Tyres:

    def __init__(self, branch, belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure
        
    def __str__(self):
        return ("Tyres: \n \tBranch: " + self.branch +
               "\n \tBelted-bias: " + str(self.belted_bias) + 
               "\n \tOptimal pressure: " + str(self.opt_pressure))
        
class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level
        
    def __str__(self):
        return ("Engine: \n \tFuel type: " + self.fuel_type +
                "\n \tNoise level:" + str(self.noise_level))
        
class Body:
    def __init__(self, size):
        self.size = size
        
    def __str__(self):
        return "Body:\n \tSize: " + self.size
        
class Car:
    def __init__(self, tyres, engine, body):
        self.tyres = tyres
        self.engine = engine
        self.body = body
        
    def __str__(self):
        return str(self.tyres) + "\n" + str(self.engine) + "\n" + str(self.body)

        
t = Tyres('Pirelli', True, 2.0)
e = Engine('Diesel', 3)
b = Body('Medium')
c = Car(t, e, b)
print(c)
""" 
Tyres: 
        Branch: Pirelli
        Belted-bias: True
        Optimal pressure: 2.0
Engine:
        Fuel type: Diesel
        Noise level:3
Body:
        Size: Medium """

""" 
Dynamic Extension
- Sometimes it's necessary to model a concept that may be a subclass of another one, but it isn't possible to know 
        which class should be its superclass until runtime.

Example
- Suppose we want to model a simple dog school that trains instructors too. 
- It will be nice to re-use Person and Student but students can be dogs or peoples. 

So we can remodel as below:
 """

class Dog:

    def __init__(self, name, year_of_birth, breed):
        self._name = name
        self._year_of_birth = year_of_birth
        self._breed = breed

    def __str__(self):
        return "%s is a %s born in %d." % (self._name, self._breed, self._year_of_birth)

kudrjavka = Dog("Kudrjavka", 1954, "Laika")
print(kudrjavka)
# Kudrjavka is a Laika born in 1954.

class Student:

    def __init__(self, anagraphic, student_id):
        self._anagraphic = anagraphic
        self._student_id = student_id

    def __str__(self):
        return str(self._anagraphic) + " Student ID: %d" % self._student_id

alec_student = Student("dsfs",1)
kudrjavka_student = Student(kudrjavka, 2)

print(alec_student)
print(kudrjavka_student)
""" 
dsfs Student ID: 1
Kudrjavka is a Laika born in 1954. Student ID: 2 """

# another example of encapsulation
class BonusDistribution:
    
    def __init__ (self,employeeId, employeeRating):
    
        self.empId = employeeId
        self.empRating = employeeRating
        self.__bonusforRatingA = "70%"  #making value private
        self.__bonusforRatingB = "60%"  #making value private
        self.__bonusforRatingC = "50%"  #making value private
        self.__bonusforRatingD = "30%"  #making value private
        self.__bonusforRatingForRest = "No Bonus" #making value private
        
        
    def bonusCalculator(self):
        
        if self.empRating == 'A':
            bonus = self.__bonusforRatingA
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'B':
            bonus = self.__bonusforRatingB
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'C':
            bonus = self.__bonusforRatingC
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'D':
            bonus = self.__bonusforRatingD
            msg = "Bonus for this employee is :"+ bonus
            return msg
        else:
            bonus = self.__bonusforRatingForRest
            msg = "Bonus for this employee is :"+ bonus
            return msg

emp1 = BonusDistribution(1232,'B')
emp2 = BonusDistribution(1342,'A')
emp3 = BonusDistribution(1031,'E')

emp2.bonusCalculator()
# 'Bonus for this employee is :70%'

emp1.bonusCalculator()
# 'Bonus for this employee is :60%'

emp3.bonusCalculator()
#'Bonus for this employee is :No Bonus'

# Let's try to change the private value of the class:

emp1._bonusforRatingB = "90%"
emp1.bonusCalculator()
# 'Bonus for this employee is :60%'

# The private attribute is not changed.

# To change the private attribute we need to define a function inside the class. Let's see how.

class BonusDistribution:
    
    def __init__ (self,employeeId, employeeRating):
    
        self.empId = employeeId
        self.empRating = employeeRating
        self.__bonusforRatingA = "70%"  #making value private
        self.__bonusforRatingB = "60%"  #making value private
        self.__bonusforRatingC = "50%"  #making value private
        self.__bonusforRatingD = "30%"  #making value private
        self.__bonusforRatingForRest = "No Bonus" #making value private
        
        
    def bonusCalculator(self):
        
        if self.empRating == 'A':
            bonus = self.__bonusforRatingA
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'B':
            bonus = self.__bonusforRatingB
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'C':
            bonus = self.__bonusforRatingC
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'D':
            bonus = self.__bonusforRatingD
            msg = "Bonus for this employee is :"+ bonus
            return msg
        else:
            bonus = self.__bonusforRatingForRest
            msg = "Bonus for this employee is :"+ bonus
            return msg       
        
    def changeBonusForRatingForRest(self,value):
        self.__bonusforRatingForRest = value

emp3 = BonusDistribution(1031,'E')
emp3.bonusCalculator()
# 'Bonus for this employee is :No Bonus'

emp3.changeBonusForRatingForRest("20%")
emp3.bonusCalculator()
# 'Bonus for this employee is :20%'

# We can see that the private attribute has now been changed and anyone can change that attribute now. 
# This is bad way of writing a method which can change an private attribute. 
# 
# Let's make the function also private so it doesnot showup for everyone.

class BonusDistribution:
    
    def __init__ (self,employeeId, employeeRating):
    
        self.empId = employeeId
        self.empRating = employeeRating
        self.__bonusforRatingA = "70%"  #making value private
        self.__bonusforRatingB = "60%"  #making value private
        self.__bonusforRatingC = "50%"  #making value private
        self.__bonusforRatingD = "30%"  #making value private
        self.__bonusforRatingForRest = "No Bonus" #making value private
        
        
    def bonusCalculator(self):
        
        if self.empRating == 'A':
            bonus = self.__bonusforRatingA
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'B':
            bonus = self.__bonusforRatingB
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'C':
            bonus = self.__bonusforRatingC
            msg = "Bonus for this employee is :"+ bonus
            return msg
        elif self.empRating == 'D':
            bonus = self.__bonusforRatingD
            msg = "Bonus for this employee is :"+ bonus
            return msg
        else:
            bonus = self.__bonusforRatingForRest
            msg = "Bonus for this employee is :"+ bonus
            return msg       
        
    def __changeBonusForRatingForRest(self,value):
        self.__bonusforRatingForRest = value

emp3 = BonusDistribution(1031,'E')
emp3.bonusCalculator()
# 'Bonus for this employee is :No Bonus'

emp3
# <__main__.BonusDistribution object at 0x000001F77358BD08>

emp3.__changeBonusForRatingForRest("20%")
""" ---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-93-2f6e3ecd0f1a> in <module>
----> 1 emp3.__changeBonusForRatingForRest("20%")

AttributeError: 'BonusDistribution' object has no attribute '__changeBonusForRatingForRest' """

""" You can see that that method cannot be accessed now. Also, the method doesnot show up in the class property:

If you know the name of the method, then you can still call the private member by using the class name as shown below:
 """

emp3._BonusDistribution__changeBonusForRatingForRest("20%")

emp3.bonusCalculator()
# 'Bonus for this employee is :20%'

""" Operator Overloading """

class multiplyNum():
    
    def __init__(self,a):
        self.a =a

a1 = multiplyNum(2)
a2 = multiplyNum(3)

#let's try and multiply both the objects
print(a1*a2)
""" ---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-98-d5b3d5e43271> in <module>
      1 #let's try and multiply both the objects
----> 2 print(a1*a2)

TypeError: unsupported operand type(s) for *: 'multiplyNum' and 'multiplyNum'


- We are getting an error because by default multiply supports only numerical values.
- We can change the function of multiply and this is what we call overloading.

- Python calls "mul" function to multiply numbers, let's overload it.
 """

class multiplyNum():
    
    def __init__(self,a):
        self.a =a
    
    def __mul__(self,other):
         return self.a*other.a

a1 = multiplyNum(2)
a2 = multiplyNum(3)

a1*a2
# 6
""" 
- Great!! now we can multiply objects. 
- We can also overide our mul function and get it do return sum instead of multiplication.
 """

class multiplyNum():
    
    def __init__(self,a):
        self.a =a
    
    def __mul__(self,other):
         return self.a+other.a  #overloading multiply method and returning sum instead of multiplication

a1 = multiplyNum(2)
a2 = multiplyNum(3)

a1*a2
# 5