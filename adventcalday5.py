import math

ticket = input("enter ticket here")
firstrow = 0
lastrow = 127
firstcolumn = 0
lastcolumn = 7
ticketrow = ticket[:7]
ticketcolumn = ticket[7:]

for elem in ticketrow: 
    if elem == "F": 
        lastrow = firstrow + (((lastrow-firstrow)//2)) #double slash is floor division
          
    elif elem == "B":
        firstrow = lastrow + (math.ceil((firstrow-lastrow)/2))  

for elem in ticketcolumn:
    if elem =="R":
        firstcolumn = firstcolumn + (math.ceil((lastcolumn-firstcolumn)/2)) 

    elif elem =="L":
        lastcolumn = lastcolumn + (math.floor((firstcolumn-lastcolumn)/2)) 

print(firstrow, firstcolumn, (firstrow * 8) + firstcolumn)

   




       

   
 
    




    










