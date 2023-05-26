def deleteFirstTwo(lst):
    lst[0] = lst[0][2:]
    lst.pop()


lst = ['12345','23456','78904']

a = lambda lst:  lst[0][2:]
print(a(lst))
