def find_tiplets(arr):
    n=len(arr)
    triplets=[]
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    triplet = sorted([arr[i],arr[j],arr[k]])
                    if triplet not in triplets:
                        triplets.append(triplet)
    return triplets
N=input("enter the no.of integres: ")
print(f"enter the {N} integres:")
arr=list(map(int,input().split()))
triplets= find_tiplets(arr)

print(f"no .fo distint triplets: {len(triplets)}")
for triplet in triplets:
    print(triplet)
