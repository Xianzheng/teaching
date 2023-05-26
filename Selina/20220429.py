'''
class Student:

    # write a __init__ method
    def __init__(self,name,scores):

        self.__ifpass = ''
        self.name = name
        self.scores = scores

        if scores >= 60:
            self.__ifpass = 'passed'
        else:
            self.__ifpass = 'not passed'

    def getIfpassed(self):
        return self.__ifpass


# Selina: SeLina, 99, passed
# Sindy: Sindy, 95, passed
# Mark: Mark, 59, not passed

#make instance of class

Selina = Student('Selina',99)
Sindy = Student('Sindy',95)
Mark = Student('Mark',59)

print(Mark.getIfpassed())

# print(Selina.ifpass) # . want to access the public attributes, but can not acess the private attribute
# print(Sindy.ifpass)
# print(Mark.ifpass)

#inheritance

# show inheritance of class
'''
# father class
class Tag:
    id = ''
    Name = ''
    Job = ''

#inherit Tag
class StudentTag(Tag):
    pass

#inherit Tag
class ProgrammerTag(Tag):
    pass

#make a instance of student Tag
tagOfSelina = StudentTag()
tagOfSelina.id = '0546'
tagOfSelina.Name = 'Selina'
tagOfSelina.Job = 'learn knowledge'
#make a instance of programmer Tag
tagOfMark = ProgrammerTag()
tagOfMark.id = '0511'
tagOfMark.Name = 'Mark'
tagOfMark.Job = 'write code'

# write three fish using inhe, using your imagination
