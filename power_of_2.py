N=input("enter the N value: ")

if not (N.isdigit() and 0 <=  int(N) < 31):
    print("enter the valid N value that (0<= N >31)")

else:
    N=int(N)
    for i in range(N+1):
        print(f"2^{i} = {2 ** i}")