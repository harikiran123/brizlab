import random 

class couponcollection:
    def generate_random(N):
        return random.randint(1,N)
    def collect_random(N):
        collect=set()
        count=0
        while len(collect) < N:
            generate_random_number=couponcollection.generate_random(N)
            count +=1
            collect.add(generate_random_number)
        return count
        

        





N= int(input("enter the N number:"))
total_no_of_collenctions=couponcollection.collect_random(N)
print(f"total random count: {total_no_of_collenctions}")