#convertTemp.py
while (1):
    temp=input("Input the temprature you want to convert:")
    if temp[-1] in ['F','f']:
        c=(float(temp[0:-1])-32)/1.8
        print("the temprature is {:.2f}C".format(c))
    elif temp[-1] in ['C','c']:
        f=float(temp[0:-1])*1.8+32
        print("the temprature is {:.2f}F".format(f))
    else:
        print("input is wrong!")
