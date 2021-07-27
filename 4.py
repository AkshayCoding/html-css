
a = int(input("Enter A Number"))
b = int(input("Enter B Number"))
c = int(input("Enter C Number"))



def largest (a,b,c):
    if (a>b) and (a>c):
        largest_num=a
    elif (b>a) and (b>c):
        largest_num=b
    else:
       largest_num=c

    print(largest_num)


largest(a,b,c)














