num=input("enter the harmonic value: ")
if not(num.isdigit() and int(num) >= 0):
    print("enter the valid positive integer value")
else:
    num=int(num)
    harmonic_sum=0.0
    for i in range(1,num+1):
        harmonic_sum += 1/i

    print(f"the N th harmonic number is {harmonic_sum:.6f}")    

