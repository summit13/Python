import read #imports read.py
import write #imports write.py
import purchase #imports purchase.py
newcust="y"
while newcust.lower()=="y": #condition to run program
    p=read.stock() #calls funtion 'stock' from read.py
    q=purchase.purchase(p) #calls funtion 'purchase' from purchase.py
    write.inventory(p,q) #calls funtion 'inventory' from write.py
    newcust=input("New customer?y/n")
print("Thank you! Please visit again.")
 
   
    






























