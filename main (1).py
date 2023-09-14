def checkLeap(Year):
    
  if((Year % 400 == 0) or
     (Year % 100 !=0) and
     (Year % 4 == 0)):
    print("given year is a leap year");
    
  else:
    print ("Given Year is not a leap Year")
    
Year = int(input("enter the number:"))

checkLeap(Year)