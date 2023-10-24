class Circle:
    
    #__init__ is a margic method,
    # this magic method run once, when this instance was make 
    def __init__(self,r):

        self.radius = r

    # self represent class it self
    def getArea(self):

        return self.radius * 3.14 ** 2

#each magic method has their own specific function
#Circle(r) # it makes a instance of Circle
a = Circle(4)

print('area of a is:',a.getArea())

b = Circle(6)

print('area of b is:',b.getArea())

c = Circle(8)
print('area of c is:',c.getArea())

# in class practice:

# consider to build class Rectangle, for __init__ method should provide width and height

# build two normal method getArea, and get circumference

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getCircumference(self):
        return 2 * (self.width + self.height)


# Example usage:
width = 5
height = 3
a = Rectangle(width, height)

area = a.getArea()

print("area of a is: ", a.getArea())
print("Circumference:", a.getCircumference())