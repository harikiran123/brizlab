import math
def caclulate_eculid_distance(x,y):
    distance = math.sqrt(math.pow(x,2)+ math.pow(y,2))
    return distance
x= int(input("enter the x coordinet: "))
y=int (input("enter the y coordinet :"))
distance = caclulate_eculid_distance(x,y)
print(f"the eculid distance of the {x} and {y} to the original (0,0) is {distance:.2f}")