m1 = int(input("Enter the marks m1 = "))
m2 = int(input("Enter the marks m2 = "))
m3 = int(input("Enter the marks m3 = "))

avg = (m1+m2+m3)/3

if avg >=70 and avg<=100:
    print("A")
elif avg >=50 and avg<70:
    print("B")
elif avg >=35 and avg<50:
    print("C")
else:
    print("FAIL")