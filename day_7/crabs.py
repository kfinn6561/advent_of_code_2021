import sys
with open('input.txt','r') as f:
    lines=f.readlines()
data=[int(i) for i in lines[0].split(',')]
data.sort()

N=len(data)
S=sum(data)
old_fuel=S-N*data[0]
for i in range(1,len(data)):
    N-=2
    S-=2*data[i-1]
    new_fuel=S-N*data[i]
    if new_fuel>old_fuel:
        print(old_fuel)
        sys.exit()
    old_fuel=new_fuel



