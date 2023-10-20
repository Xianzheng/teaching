class Info:
    # cost = ''
    def __init__(self): # __specificName__ magic method
        
        self.cost = '4$'


    def __str__(self): # 
        return 'the cost is '+self.cost


# __init__ magic method means when instance of class was created
# __init__ method will run once
a = Info() #  a is instance of class

# __str__ str magic method means when you print instance , what will happen
print(a)

