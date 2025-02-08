import math
def cal_wind_chill(t,v):
    wind_chill = 35.75 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)

    return wind_chill
t = float(input("enter the temparature in f_heat(<=50)"))
v = float(input("enter the speed (3<= v <=120)"))
if not (abs(t)<=50 and v >= 3 and v <= 120):
    print("error pleas enter the correct values")
else:
    wind_chill = cal_wind_chill(t,v)
    print(f"the wind chill is: {wind_chill:.2f}")