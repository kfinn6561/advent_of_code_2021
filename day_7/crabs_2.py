import math
with open('input.txt','r') as f:
    lines=f.readlines()
data=[int(i) for i in lines[0].split(',')]
data.sort()

N=len(data)
S=sum(data)
S2=sum([x**2 for x in data])
current_N=N
current_S=S
best_fuel=math.inf
i=0
for x in range(data[-1]):
    while x>data[i]:
        current_N-=2
        current_S-=2*data[i]
        i+=1
    fuel=(current_S-current_N*x+N*(x**2)+S2-2*x*S)/2
    if fuel<best_fuel:
        best_fuel=fuel
print(int(best_fuel))



