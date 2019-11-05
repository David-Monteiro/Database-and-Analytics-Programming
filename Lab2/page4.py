###Page 4


print("Input a year:\n")
inputYear = int(input())
isLeapYear = False

if inputYear % 400 == 0:
    isLeapYear = True
elif inputYear % 100 == 0 :
    isLeapYear = False
elif inputYear % 4 == 0 :
    isLeapYear = True

print(isLeapYear)


