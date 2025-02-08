import random
num_flips=int(input("enter the no.of times the coin is tossed: "))
if num_flips <= 0:
    print("enter some postive value")
else:
    head=0
    tails=0
    for i in range(num_flips):
        if  random.random() < 0.5:
            tails+=1
        else:
            head+=1
    heads_presentage= (head/num_flips)*100
    tails_presentage= (tails/num_flips)*100
    print(f"head: {head},{heads_presentage:.2f}")
    print(f"tails: {tails},{tails_presentage:.2f}")

    


