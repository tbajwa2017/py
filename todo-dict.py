#!/usr/bin/python
# Author: Tahir Bajwa
# Date:	  03.26.2018
import os
import re
records={}
ans=True
os.system('clear')
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
      name1=raw_input("Enter name: ")
      address1=raw_input("Enter address: ").title()
      records.update({name1.title():address1.title()})
      print("\n Record Added") 
    elif ans=="2":
      os.system('clear')
      try:
         #records.remove( rm1 = raw_input("Enter the name to be deleted: "))
         rm1 = raw_input("Enter the name to be deleted: ").title()
         del records[ rm1 ]
         print("\n Record Deleted: " + rm1.title()) 
      except:
         print "Record not deleted ( Record Not found ) : " + rm1
    elif ans=="3":
      os.system('clear')
      if records:
         print("\n Records Found") 
         #print records
         for key,value in records.items():
            print key + " : " + value
      else:
         print("\n No Records Found")
    elif ans=="4":
      #print("\n Records Found") 
      #print records
      os.system('clear')
      found = "false"
      j = raw_input("Enter record to be searched: ")
      for key, value in records.items():
          if re.search(j.lower(),key.lower()):
            print "Matching record found: " + key + " : " + value
            found = "true"
      if found == "false":
         print "Record not found: " + j
      #print records.get(j,"Record not found: " + j)
    elif ans=="5":
      print("\n Goodbye") 
      break
    else:
      print("Wrong option selection. ") 
      os.system('sleep 2')
      os.system('clear')
      ans = True
