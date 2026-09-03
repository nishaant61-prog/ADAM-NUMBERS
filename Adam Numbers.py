for i in range (int(input('enter lower limit:')),int(input('enter upper limit:'))):
    g=int(max(str(i)))                                                               #"no carry" rule
    if g<=3:
        h=int(str(i)[::-1])                                                          #reversing the number i
        if i<=h:                      
            k=int(str(i**2)[::-1])                                                   #reversing the number i**2
            if h**2==k:
                print([(i,i**2),(h,k)])
