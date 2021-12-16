import math
input_data=[]
with open('input.txt','r') as f:
    for line in f:
        temp=[]
        for char in line.strip():
            temp.append(int(char))
        input_data.append(temp)

N=len(input_data)
M=len(input_data[0])

data=[[0 for i in range(5*M)] for j in range(5*N)]
for x in range(5):
    for y in range(5):
        for i in range(N):
            for j in range(M):
                data[i+N*x][j+M*y]=(input_data[i][j]+x+y-1)%9+1

N*=5
M*=5

lowest_risk=[[math.inf for i in range(M)] for j in range(N)]

def get_lowest_risk(i,j):
    if i==0 and j==0:
        return 0
    risks=[]
    if i>0:
        risks.append(lowest_risk[i-1][j])
    if j>0:
        risks.append(lowest_risk[i][j-1])
    if i<N-1:
        risks.append(lowest_risk[i+1][j])
    if j<M-1:
        risks.append(lowest_risk[i][j+1])
    return min(risks)+data[i][j]

def get_neighbours(i,j):
    out=[]
    if i>0:
        out.append((i-1,j))
    if j>0:
        out.append((i,j-1))
    if i<N-1:
        out.append((i+1,j))
    if j<M-1:
        out.append((i,j+1))
    return out

to_check=[(0,0)]
while len(to_check)>0:
    i,j=to_check.pop(0)
    lr=get_lowest_risk(i,j)
    if lr<lowest_risk[i][j]:
        lowest_risk[i][j]=lr
        if lr+(N-i-1)+(M-j-1)<lowest_risk[-1][-1]:
            to_check+=get_neighbours(i,j)

print(lowest_risk[-1][-1])