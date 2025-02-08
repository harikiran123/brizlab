import random
def cal_the_winsandloss(stack,goal,trails):
    wins=0
    total_bets=0
    for i in range(trails):
        cash=stack
        while 0<cash<goal:
            total_bets += 1
            if random.random()<0.5:
                cash+=1
            else:
                cash-=1
        if cash == goal:
            wins+=1
    return wins,total_bets


stack = int(input("enter the stack value: "))
goal = int(input("enter the goal value: "))
trails = int(input("enter the no.of trails: "))

wins,total_bets=cal_the_winsandloss(stack,goal,trails)
loss_count=trails-wins
win_per=(wins/trails)*100
loss_per=(loss_count/trails)*100
avg_bets=total_bets / trails if trails>0 else 0
print(f"no.of trains: {trails}")
print(f"no.of wins : {wins}")
print(f"no.of loss: {loss_count}")
print(f"persentage of win: {win_per:.2f}")
print(f"persentage of loss: {loss_per:.2f}")
print(f"avrage bet per tails: {avg_bets:.2f}")

