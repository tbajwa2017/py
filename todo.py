#!/usr/bin/python
# Author: Tahir Bajwa
# Date:	  03.26.2018
import os
import re
records=[]
ans=True
os.system('clear')
def atof(text):
    try:
        retval = float(text)
    except ValueError:
        retval = text
    return retval

def natural_keys(text):
    return [ atof(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', text) ]

while ans:
    print ("""
    ==============================
    |TODO DATA STORE MEMORY BASED|
    ==============================
    | 1.Add a Record             |
    | 2.Delete a Record          |
    | 3.Show all Records         |
    | 4.Search all Records       |
    | 5.Exit/Quit                |
    ==============================
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1": 
      os.system('clear')
      #records.append( raw_input("Enter the name: ").title())
      rec1=raw_input("Enter the name: ").title()
      if re.search('\-.*',rec1):
         print "Record not added"
      else:
         records.append(rec1.title()) 
      print("\n Record Added") 
    elif ans=="2":
      os.system('clear')
      try:
         #records.remove( rm1 = raw_input("Enter the record to be deleted: "))
         rm1 = raw_input("Enter the record to be deleted: ")
         records.remove( rm1.title() )
         print("\n Record Deleted: " + rm1.title()) 
      except:
         print "Record not deleted ( Record Not found ) : " + rm1
    elif ans=="3":
      os.system('clear')
      if records:
         print("\n Records Found") 
         #print records.sort()
         #for x in sorted(int(records)):
         #    print x
         #records = [ int(x) for x in records]
         #records.sort(key=int)
         records.sort(key=natural_keys) 
         print records
      else:
         print("\n No Records Found")
    elif ans=="4":
      #print("\n Records Found") 
      #print records
      os.system('clear')
      found = "false"
      j = raw_input("Enter record to be searched: ")
      for i in records:
         #if i == j:
          if re.search(j.lower(),i.lower()):
            print "Matching record found: " + i
            found = "true"
      if found == "false":
         print "Record not found: " + j
    elif ans=="5":
      print("\n Goodbye") 
      break
    else:
      print("Wrong option selection. ") 
      os.system('sleep 2')
      os.system('clear')
      ans = True
