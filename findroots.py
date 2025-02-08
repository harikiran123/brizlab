import math
def find_roots(a,b,c):
    delta = math.pow(b,2)-4*a*c
    if delta > 0:
        root1=(-b + math.sqrt(delta)) / (2*a)
        root2 =(-b - math.sqrt(delta))/(2*a)
        return f"roots are real and distint: root1 = {root1:.2f} and root2= {root2:.2f}"
    elif delta == 0:
        root= -b/(2*a)
        return f"roots are real and equal:root = {root:.2f}"
    else:
        real_part= -b/(2*a)
        imaginary_part=math.sqrt(-delta)/(2*a)
        return f"roots are complex: root1 = {real_part:.2f} + {imaginary_part:.2f}i, root2= {real_part:.2f} - {imaginary_part:.2f}i"

    
a = float(input("enter the a value (a!=0) : "))
b = float(input("enter the b value : "))
c = float(input("enter the c value: "))
if a == 0:
    print("error a should not be zeor")
else:
    result=find_roots(a,b,c)
    print(result)