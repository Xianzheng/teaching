'''
import random

num = random.randint(1, 10)
attempts = 0

print("A number has been generated")

while attempts < 5:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == num:
        print("You guessed the correct number")
        break

    if guess < num:
        print("Too low")

    if guess > num:
        print("Too high")

if attempts > 5:
    print("You've run out of attempts.")
    print("The number was", num)

# java or js loop
for (i =0 ; i< 5; i++){

}

for i in range(1,11):
    print(i)

# print all odd numbers between 1- 10

for i in range(1,11,2):
    print(i)

# range(start, stopby, step)

# print all odd numbers between 1- 9
for i in range(1,9,2):
    print(i)
# if you don't indicate third params for range(), step default 1
for i in range(1,11):
    print(i)



# print all number 25,28,31,14,26

# print the sum of 25,28,31,14,26

# print all odd numbers between 1 - 20

# print all even numbers between 1 - 20



# break, continue
for i in range(1,30,3):
    # only print a number blow 18

    if i >= 18:
        break
    print(i)

    # if put in print before judge block , print first then judge
    # if put in print after judge block , judge first then print


for i in range(1,11):

    if i == 3 or i == 6:
        continue

    print(i)

# get factorial 3! = 3 * 2 * 1, 5 ! = 5 * 4 * 3 * 2 * 1

# 5 ! , 5 * 3 * 2 * 1

# get value of 20 ! , not times 14, not times 10, not times 8 using continue

result = 1
for num in range(1, 21):
    if num == 14 or num == 10 or num ==8:
        continue # jump
    result *= num

print(result)

factorial = 1
num0 = [14, 10, 8]

for num in range(1, 21):
    if num not in num0:
        factorial *= num

print(factorial)

'''
# get value of 20 !, but we only do continuously times until to 10 using break

# continue , break only can use in a loop

# if put in print before judge block , print first then judge
# if put in print after judge block , judge first then print

# break, continue
# break: break a whole loop
# continue: will jump the content after continue
for i in range(1,30,3):
    # only print a number blow 18
    print(i)
    if i >= 18:
        continue




'''
# choose use continue or break to do
1. print some thing like 1 2 3 4 5 7 8 10

2. print m a f pass f pass n g:
# for i in 'markfang':
#     print(i)
# consider using if else and continue

3. conside how to print 10 9 8 7 6 5 4 3 2 1
# hint: range(start, stop by,step)

4. conside how to print 10 9 8 7 5 4 3 1
'''

