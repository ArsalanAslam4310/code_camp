class Person:
    '''made class of person 
    '''
    def __init__(self,name,age,rool_no):
        self.name = name
        self.age = age
        self.rool_no=rool_no

person1=Person("arslan",22,4)
print(person1.name,person1.age,person1.rool_no)
