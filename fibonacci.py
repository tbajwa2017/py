t1 = 0
t2 = 1

num1 = int(raw_input("Enter the maximum number : "))

print "Fibonacci Series: "
nextterm = 0
for i in range(0,9999999):
   if t1 <= num1:
      print t1 
      nextterm = t1 + t2
      t1 = t2
      t2 = nextterm


