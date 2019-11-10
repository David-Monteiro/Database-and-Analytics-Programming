###Exercise 2

def isFib(x, y, z):
    if x == 0 or x == 1:
        return True
    elif lambda x, y, z: (z + y) - x == 0:
        return True
    else: return False


myList = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 7, 89, 144]
for num in myList:
    index = myList.index(num)
    print (str(num) + " " + str(myList[index-1]) + " " +  str(myList[index-2]))
    print(bool(isFib(num, myList[index-1], myList[index-2])))



