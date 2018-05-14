#convertTemp.py 华氏度 摄氏度温度转换，输入温度，通过f和c判断用户输入的是华氏温度还是摄氏温度，然后开始转换
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
