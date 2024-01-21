str1 = ""
for i in range(1,100):
 if i%15 == 0:
  str1 = str1 + str(i)  +":FizzBuzz "
 if i%3 == 0:
  str1 = str1 + str(i)  +":Fizz "
 elif i%5 == 0:
  str1 = str1 + str(i)  +":Buzz "
 else:
  str1 = str1 + str(i) + " "

print(str1)