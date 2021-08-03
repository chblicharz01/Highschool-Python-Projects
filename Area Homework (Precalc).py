import math
area = 0
while True:
    a = float(input("Enter A Value:"))
    b = float(input("Enter B Value:"))
    c = float(input("Enter C Value:"))
    if a ==0 and b == 0 and c == 0:
        break
    else:
        area = (.5 *(math.sin(math.radians(c))))  * a * b
        print(area)
        

        
