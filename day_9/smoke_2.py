from collections import defaultdict

with open('input.txt','r') as f:
    lines=f.readlines()

N=len(lines)
M=len(lines[0].strip())

data=[[9]*(M+2)]#padding with 9s
for line in lines:
    data.append([9]+[int(i) for i in line.strip()]+[9])
data.append([9]*(M+2))

def get_neighbours(i,j):
    return [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

def get_basin(i,j):
    out=defaultdict(list)
    size=0
    to_check=[(i,j)]
    while len(to_check)>0:
        x,y=to_check.pop()
        if (y in out[x]) or data[x][y]==9:
            continue
        out[x].append(y)
        size+=1
        to_check+= get_neighbours(x,y)
    return size,out

checked=defaultdict(list)
basin_sizes=[]
for i in range(1,N+1):
    for j in range(1,M+1):
        if j not in checked[i]:
            basin_size,new_checked=get_basin(i,j)
            basin_sizes.append(basin_size)
            for k in new_checked.keys():
                checked[k]+=new_checked[k]

basin_sizes.sort()
print(basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3])
