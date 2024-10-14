ip1 = int(input("Enter first input = "))
ip2 = int(input("Enter second input = "))
cntEven = 0
cntOdd = 0
for i in range(ip1,ip2+1):
    if i%2 == 0:
        print(i)
        cntEven+=1
    else:
        cntOdd+=1
else:
    print("Cnt of even num  = ",cntEven)
    print("Cnt of odd num  = ", cntOdd)
