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
    
alec = Person("akshay", "kumar", 2021)
print(alec)
print(alec.age(2022))
print(alec.skin_color)
print(Person.skin_color)
""" 
akshay kumar was born in 2021 .
1 
white
white"""