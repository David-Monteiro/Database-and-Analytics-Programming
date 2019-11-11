#Exception Handling Exercise

filename = "hello.txt"
file = open(filename, "w")

try:
   for line in file:
       print(line)
except io.UnsupportedOperation:
   pass
finally:
  print("not readable")

file.close()
