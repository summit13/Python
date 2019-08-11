def stock(): #function 'stock' is defined
    file=open("stock.txt","r")
    list_=[] 
    read=file.readlines() #write each line as element in list
    for x in read:
        list_.append(x.replace("\n","").split(","))
    file.close() #closing file
    for i in range(len(list_)):
        print("Product",list_[i][0],"\t Price",list_[i][1],"\t Quantity",list_[i][2])
    return list_  #final list is returned to function
