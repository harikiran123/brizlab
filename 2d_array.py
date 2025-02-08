import sys
def read_the_array(row,colm,data_type):
    array=[]
    print(f"enter the {row * colm} elements")
    for i in range(row):
        row = list(map(data_type,input().split()))
        array.append(row)
    return array
def print_array(array):
    sys.stdout.write("\n2D Array Output:\n")
    for row in array:
        sys.stdout.write(" ".join(map(str, row)) + "\n")




    

M=int(input("enter the no.of row: "))
N=int(input("enter the no.of colm: "))
data_type = eval(input("Enter data type (int/float/bool): "))
matrix=read_the_array(M,N,data_type)
print_array(matrix)