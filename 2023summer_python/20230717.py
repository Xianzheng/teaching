'''
hw:
email = "mark.ffang@gmail.com"
#index   012345...
# 1. loop all item from eamil

# 2. get useful information, first name, last name, which email used

# 3. get all odd item letter # akf ...

# 4. get all even  item letter # mr. ...
'''

# string ， slice
email = "mark.ffang@gmail.com"
#index   0123456789012345
# 1. loop all item from eamil

# first method: loop all item
# for item in email:
#     print(item)

#second method: use each index to access the item
# len(email): to get the length of email: 20
# for index in range(len(email)):
#     print(email[index])

# 2. get useful information, first name, last name, which email used
email = "mark.ffang@gmail.com"
# first method: using split
# rawMeterial = email.split("@")
# print(rawMeterial)
# email = rawMeterial[1].split(".")[0]
# print(email)
# firstName = rawMeterial[0].split(".")[0]
# print(firstName)
# lastName = rawMeterial[0].split(".")[1]
# print(lastName[1:])

# second method: use slice
# email = "mark.ffang@gmail.com"
# firstName = email[0:4]
# print(firstName)
# lastName = email[6:10]
# print(lastName)
# email = email[11:16]
# print(email)

# 3. get all odd item letter # akf ...
# first method: use if
# for index in range(len(email)):
#     if index % 2 != 0:
#         print(email[index])

# second method:
for index in range(1,len(email),2):
    print(email[index])

'''
hw for review class:

email1: chncloudli@foxmail.com
email2:soleil_li@icloud.com

Get the the useful information for email1 and email2,get the even letter for both 

'''






