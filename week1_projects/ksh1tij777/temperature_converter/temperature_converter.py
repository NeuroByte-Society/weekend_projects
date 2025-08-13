a=int(input("choose 1 for celsius to fahrenheit , 2 for fahrenheit to celsius,3 for celsius to kelvin, 4 for kelvin to celsius \n"))

if a==1:
    c=float(input("enter temperature in celsius"))
    f=(c*9/5)+32
    print("temperature in fahrenheit is",f)

elif a==2:
    f=float(input("enter temperature in fahrenheit"))
    c=(f-32)*5/9
    print("temperature in celsius is",c)

elif a==3:
    c=float(input("enter temperature in celsius"))
    k=c+273.15
    print("temperature in kelvin is",k)

elif a==4:
    k=float(input("enter temperature in kelvin"))
    c=k-273.15
    print("temperature in celsius is",c)

else:
    print("invalid input, please choose a valid option")