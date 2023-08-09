'''
2.
testDic = {'English':90,'Math': 95,'Python': 89,'Gym':99 }
# using testDic to get which course get max scores and which course get min scores
# hint : max(list) to get highest value of list
#        min(list) to get lowest value of list

3. do J2 of CCC J2 problem of CCC 2019
#https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf



testDic = {'English':90,'Math': 95,'Python': 89,'Gym':99 }

soredDic = sorted(testDic,key=testDic.get)
print(soredDic)
print(soredDic[0]) # min
print(soredDic[-1])# max


# +++===!!!!
# 0123456789
# 3 + 3 = 4 !

3.1415555
1 3 1 . 1 1 1 4 1 1 4 5
'''

str1 = '+++===!!!!'
count = 1
for i in range(len(str1) - 1):
    # since the last index can not commpare with last index + 1
    # our index end in previous index of last index
    #we always compare index and next index
    if str1[i] == str1[i + 1]:
        # current element equals next element do
        # add count by 1
        
        pass

    if str1[i] != str1[i + 1]:
        # current element not equals next element do
        # print count: count
        # print sign: str1[i]
        # reinitialize count: count = 1
        pass
        

    if i == len(str1) - 2:
        # current index is previous index of last index
        # print count: count
        # print sign: str1[i]
        pass
'''
1.
# do CCC 2019 J3 
# link：https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2019/stage%201/juniorEF.pdf

Sample Input
4
+++===!!!!
777777......TTTTTTTTTTTT
(AABBC)
3.1415555
Output for Sample Input
3 + 3 = 4 !
6 7 6 . 12 T
1 ( 2 A 2 B 1 C 1 )
1 3 1 . 1 1 1 4 1 1 4 5

# use range to
2. print number for 45 43 42 .... 21

3. string1 = 'Pascal Xavier'
print String1 inorder, reverse order
# print using index to print
# print using for loop

# function convert string <=> number, string <=> lst, string <=> dic

'''



