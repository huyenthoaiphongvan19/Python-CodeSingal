# Here is my solution to this problem in PYTHON. I've tried to explain each step so that you can apply this to any language

# My Solution:

# a) First, sorting the array from least to greatest would make this process simpler, thankfully there's a built in method for that ( called .sort())

# b) fL loops from 0 to the second last element in the array (also look at the while statement)

# c) sL loops from 1 to the last element in the array (also look at the while statement)

# d) the differences variable keeps track of the number of statues needed to fill in between two consecutive numbers 
# so say the numbers were 5 and 9, differences would hold 3 because you need three statues (6,7,8) to go in-between those two numbers.

# e) Inside the while loop, it records the number of statues that can go in-between every adjacent pairs.

# f) Inside the if statement, if difference between two consecutive number is more than one 
# (ie. The difference between 6 and 7 is 1, but you cant put a statue in-between, so we look for 
# a difference of higher than 1 for each consecutive pairs).

# g) fL and sL are incremented by 1 as they continue the loop.

# def solution(statues):


statues = [6, 2, 3, 8]
statues.sort(reverse=True)
print(statues)
sL = 0
for i in range(0,len(statues)-1):
    if statues[i] - statues[i+1] != 1:
        sL += statues[i] - statues[i+1] - 1
print(sL)