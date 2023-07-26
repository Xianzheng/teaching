'''
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
'''
#-20
score = 10

if score >= 80:
    print('A')
elif 60 >= score > 80:
    print('B')
elif 50 >= score > 66:
    print('C')
elif score >= 45 and score < 50:
    print('D')
elif score >= 25 and score < 45:
    print('E')
elif score < 25:
    print('F')


'''
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.
'''

# cost = 2

# beforeDiscount = 1000 * 2

# print(beforeDiscount)

# discount = beforeDiscount * 0.1

# print(discount)

# totalCost = beforeDiscount - discount

# print(totalCost)

# cost
# quantity

cost = 2

quantity = 999

if quantity >= 1000:
    beforeDiscount = cost * quantity
    discount = beforeDiscount * 0.1
    totalCost = beforeDiscount - discount
else:
    totalCost = cost * quantity

print(totalCost)
