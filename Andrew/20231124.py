'''
lst = [1,2,3,4,5,6]

# use index to loop it all

for index in range(len(lst)):
    if lst[index] == 5:

        lst[index] = 7

# for item in lst:
#     if item == 5:
#         item = 7
#     print(item)
print(lst)


question:
use for loop to change item = 5 to 7
'''

'''
4
+++===!!!!
777777......TTTTTTTTTTTT
(AABBC)
3.1415555


'''

'''
make input, store our input
'''
storage = [input() for i in range(int(input()))]

'''
make parsing , deal each input
'''

def parse(line):
    count = 1

    for i in range(len(line) - 1):

        part1 = line[i]
        part2 = line[i + 1]

        if part1 == part2:
            count += 1
                
        if part1 != part2:
            print(count, part1, end=' ')
            count = 1
        
        if i == len(line)-2:
            print(count, part1)
'''
make output
'''
for line in storage:
    parse(line)

parse('+++===!!!!')
parse('777777......TTTTTTTTTTTT')
parse('(AABBC)')
parse('3.1415555')


'''
HW:
1.do CCC 2019 J3 again using your thinking

2. repeat do input first then output, do CCC 2019 J2

3. Problem J3: Are we there yet? DO INPUT FIRST

LINK: https://www.cemc.uwaterloo.ca/contests/computing/past_ccc_contests/2018/stage%201/juniorEF.pdf

'''