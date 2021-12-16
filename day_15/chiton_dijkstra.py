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
visited=[[False for i in range(M)] for j in range(N)]

def get_neighbours(i,j):
    out=[]
    if i>0 and not visited[i-1][j]:
        out.append((i-1,j))
    if j>0 and not visited[i][j-1]:
        out.append((i,j-1))
    if i<N-1 and not visited[i+1][j]:
        out.append((i+1,j))
    if j<M-1 and not visited[i][j+1]:
        out.append((i,j+1))
    return out

to_check=[(0,0)]
def get_next_point():
    out=min(to_check,key=lambda p:lowest_risk[p[0]][p[1]])
    to_check.remove(out)
    return out

lowest_risk[0][0]=0
while len(to_check)>0:
    i,j=get_next_point()
    if i==N-1 and j==M-1:
        print(lowest_risk[i][j])
    visited[i][j]=True
    lr=lowest_risk[i][j]
    for point in get_neighbours(i,j):
        x,y=point
        if lowest_risk[x][y]==math.inf:
            to_check.append(point)
        lowest_risk[x][y]=min(lr+data[x][y],lowest_risk[x][y])