def inventory(x,y):
    list_=x
    dist=y

    for k in dist.keys():
        if k=="phone":
            list_[0][2]=str(int(list_[0][2])-dist['phone']) 
        elif k=="laptop":
            list_[1][2]=str(int(list_[1][2])-dist['laptop'])
        else:
            list_[2][2]=str(int(list_[2][2])-dist['hdd'])
    print (x)

    file=open("stock.txt","w")  #opens txt file in write mode.     
    for row in x:
        file.write(str(",".join(row))) #write to the file
        file.write("\n")  #line break         
    file.close() #close file
    return






