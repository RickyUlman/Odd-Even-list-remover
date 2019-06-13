# Author:           Richard n Barnes iii
# Title:            Exercise 8 - 2
# Purpose:          Removes odd or even numbers from a list

intList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
nn = True

# removes odd numbers from list
def getEven(list):
    for i in list[:]:
                if i % 2 != 0:
                      list.remove(i)
    return list

# removes even numbers from list
def getOdd(list):
    for i in list:
        if i % 2 == 0:
            list.remove(i)
    return list 

# function with boolean arg
def display(list,n):
    if n is True:
        return getEven(intList)
    else:
        return getOdd(intList)


print(display(intList,nn))