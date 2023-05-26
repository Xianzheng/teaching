# type code create a lst, append 'Mark','Selina','Lucas' into it

# when you finish please let me know

lst = []
lst.append('Lucas')
lst.append('Mark')
lst.append('Selina')
print(lst)

# now we want lst rotated'
#for example
#first time ['Lucas', 'Mark', 'Selina']
#secode time ['Selina','Lucas', 'Mark']
# third time ['Mark','Selina','Lucas']

# try to do it? I think you can do it

# actually each time we pop the last element and put it int0 header

#if we want it run multiple times then put it into a loop

for i in range(3):
    popedElement = lst.pop()
    lst.insert(0,popedElement)
    print(lst)