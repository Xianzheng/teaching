# if you get any question you can type on group chat 

#question1: how to create a list, we talked yesterday?

#ok create list we use

lst = []

#question2: how to add something to list

# if we want to add 'apple' to lst how to do it? use code?

lst.append('apple')

lst.append('banana')

lst.append('cherry')

lst.append('peach')

print(lst)

#question2: how about we want to take peach out of lst?

# if we just take 'peach' out of lst


# print(lst)

# if we want to know which element we poped , we can assign lst.pop() to element

element = lst.pop()

print(element)

# actually, 'peach' already have been taken out from lst

print(lst)

# question: have to add 'peach' to the top of lst

lst.insert(0,element) # 0 mean the top of lst

print(lst)