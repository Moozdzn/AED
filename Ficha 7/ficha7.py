from random import randrange

#Exercise 1 
# 
# O(n^2)

def lowestInt_On(number_list):
    lowest_number = number_list[0]
    for x in number_list:
        if lowest_number > x:
            lowest_number = x
    return lowest_number

#O(n)
def lowestInt_On2(number_list):
    lowest_number = number_list[0]
    for x in number_list:
        found = True
        for y in number_list:
            if x > y:
                found = False
        if found:
            lowest_number = x
    return lowest_number

my_list = [2,4,7,0,6]

#Testing
#print(lowestInt_On(my_list))
#print(lowestInt_On2(my_list))



#Exercise 2 

#a)   T(n) = n^2 ; O(n^2)

#b)   T(n) = n ; O(n)

#c)   T(n) = 1 + 2n = 2n + 1 ; O(log n) 

#d)   T(n) = n^3 ; O(n^3)

#e)   T(n) = n + n + n = 3n ; O(3n) = O(n) - as we can ignore constant n 

#Exercise 3

random_list = [randrange(100) for x in range(50)]
my_list = [2,4,7,0,6]

def kLowestInt(number_list, k):
    new_list = []
    
    while len(new_list) < k:
        lowest_number = number_list[0]
        lowest_number_index = 0
        for i in range(len(number_list)):
            if number_list[i] < lowest_number:
                lowest_number = number_list[i]
                lowest_number_index = i
        new_list.append(lowest_number)
        number_list.pop(lowest_number_index)
    return new_list

#Testing
print(random_list)
print(kLowestInt(random_list,8))
print(random_list)

