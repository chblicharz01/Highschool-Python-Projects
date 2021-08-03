import math
x1 = float (input("What is the first x equal to?"))
y1 = float(input("What is the first y equal to?"))
x2 = float (input("What is the second x value equal to?"))
y2 = float (input("What is the second y value equal to?"))

factor1 = ((x2 - x1)**2)
factor2 = ((y2 - y1)**2)
distance = math.sqrt(factor1 + factor2)
print("The distance is ",distance, "\n\n\n")
input("Press any enter to exit...")
            
