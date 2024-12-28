day=int(input("Enter the month:"))
mon=int(input("Enter the year:"))
if(day==1):
   print("31 days")
#elif(day==2):
#    print("28 days")
elif((day==2) and ((mon%4==0)  or ((mon%100==0) and (mon%400==0)))):
    print("Number of days is 29")
elif(day==2):
    print("28 days")
#elif((day==2) and ((mon%4==0)  or ((mon%100==0) and (mon%400==0)))):
 #    print("29 days")
elif(day==3):
   print("31 days")
elif(day==4):
   print("30 days")
elif(day==5):
   print("31 days")
elif(day==6):
   print("30 days")
elif(day==7):
   print("31 days")
elif(day==8):
   print("31 days")
elif(day==9):
   print("30 days")
elif(day==10):
   print("31 days")
elif(day==11):
   print("30 days")
elif(day==12):
   print("31 days")
else:
   print("Invalid Input")
