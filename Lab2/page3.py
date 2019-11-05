###Page 3


print("Input a random number:\n")
inputN= int(input())
if inputN % 2 != 0 :
    print("Weird!\n")
elif inputN % 2 == 0 and inputN >= 2 and inputN <= 5 :
    print("Not Weird!\n")
elif inputN % 2 == 0 and (inputN >= 6 and inputN <= 20) :
    print("Weird!\n")
elif inputN % 2 == 0 & inputN >19 :
    print("Not Weird!\n")