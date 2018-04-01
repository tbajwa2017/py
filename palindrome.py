str1 = raw_input("Enter string to check for palindrome: ")

str2 = str1.lower().replace(" ","")
 
str3a=""
for i in str2:
 if i.isalpha():
  str3a = str3a + i


str3 = str3a[::-1]

if str2 == str3:
 print "The string " + str1 + " is a Palindrome"
else:
 print "The string " + str1 + " is not a Palindrome"

str4=""
