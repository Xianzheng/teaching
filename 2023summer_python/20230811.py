# inherited
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print('Animal can bark')
# extends Animal
class Dog(Animal):
    
    def bark(self):
        print('bow-wow')

class Cat(Animal):
   
   def bark(self):
       print('meow')

class Bird(Animal):
    pass

dog = Dog('Dog1',10)
cat = Cat('Cat1',10)

#DRY(don't repeat yourself)
dog.bark()
cat.bark()


# make instance of Cat and Bird, give some attribute
'''
hw:
create class using inherited from father class
do override
'''
