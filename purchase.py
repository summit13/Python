def purchase(p): #function with parameter 'p' is declared
    list_=p
    custname=input("Enter name of customer") #enter customer name
    items={}
    condition="y"
    while condition.lower()=="y": #condition
        prod=input("Enter name of product") #enters name of product 
        prod1=prod.lower()
        if prod1==list_[0][0].lower() or prod1==list_[1][0].lower() or prod1==list_[2][0].lower():
            condition1=False
            while condition1==False:
                try:
                    numprod=int(input("Enter number of product"))
                    condition1=True
                except:
                    print("You need to enter integer value.")
            if prod==list_[0][0].lower() and numprod<int(list_[0][2]):
                items[prod1]=numprod
            elif prod==list_[1][0].lower() and numprod<int(list_[1][2]):
                items[prod1]=numprod
            elif prod==list_[2][0].lower() and numprod<int(list_[2][2]):
                items[prod1]=numprod
            else:
                print("Sorry! We dont have adequate number of products")
            condition=input("Do you want more products?(y/n)")
        else:
            print("Sorry! We do not have the product that you are searching for.")
            ans=input("Continue??y/n")
    print("Items")
    print(items)
    #for total cost of product
    total=0
    for k in items.keys(): #loop into every item in dicttionary 
        if k==list_[0][0].lower(): #calculates cost if product is phone
            phoneprice=int(list_[0][1])
            phoneqty=int(items[k])
            phonecost=phoneprice*phoneqty
            total+=phoneprice*phoneqty
            print("Phone----",phonecost)
        elif k==list_[1][0].lower(): #calculates cost if product is laptop
            laptopprice=int(list_[1][1])
            laptopqty=int(items[k])
            laptopcost=laptopprice*laptopqty
            total+=laptopprice*laptopqty
            print("Laptop----",laptopcost)
        else:                       #calculates cost if product is hdd
            hddprice=int(list_[2][1])
            hddqty=int(items[k])
            hddcost=(hddprice*hddqty)
            total+=(hddprice*hddqty)
            print("HDD----",hddcost)
    print("Total=",total) #displays subtotal
    dis=float(input("Enter discount in percentage"))
    total1=float(total-(dis/100)*total) #calculates grand total  
    print("Discount%=",dis)
    print("Discount amount=",total*(dis/100))
    print("Grand Total=",total1)#displays grand total  

    #for invoice
    import datetime #imports date and time for unique invoice id
    dt=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    dt1=str(dt)
    file=open(dt1+".txt","w")
    file.write("**************************INVOICE**************************")
    file.write("\n")
    file.write(str("Name: "+str(custname)+"                       Date: "+dt1))
    file.write("\n")
    file.write("\tProducts \t Qty \t Rate \t Price")
    file.write("\n")

    for k in items.keys():
        if k=="phone":
            file.write(str("\t"+str(k)+" \t\t "+str(items['phone'])+" \t "+str(list_[0][1])+" \t "+str(phonecost)))
            file.write("\n")
        elif k=="laptop":
            file.write(str("\t"+str(k)+" \t\t "+str(items['laptop'])+" \t "+str(list_[1][1])+" \t "+str(laptopcost)))
            file.write("\n")
        else:
            file.write(str("\t"+str(k)+" \t\t "+str(items['hdd'])+" \t "+str(list_[2][1])+" \t "+str(hddcost)))
            file.write("\n")

    file.write("\n")
    file.write("\t\t\t\t Total:  "+str(total))
    file.write("\n")
    file.write("\n")
    file.write("\t\t\t\t Discount% :"+str(dis))
    file.write("\n")
    file.write("\n")
    file.write("\t\t\t\t Grand Total:"+str(total))
    file.write("\n")
    file.write("\n")
    file.write("*************************THANK YOU!!!*************************")
    file.close()
    return items
