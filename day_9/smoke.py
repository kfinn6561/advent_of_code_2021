with open('input.txt','r') as f:
    lines=f.readlines()

N=len(lines)
M=len(lines[0].strip())

data=[[10]*(M+2)]#padding with 10s
for line in lines:
    data.append([10]+[int(i) for i in line.strip()]+[10])
data.append([10]*(M+2))


out=0
for i in range(1,N+1):
    for j in range(1,M+1):
        if data[i][j]<data[i][j-1] and data[i][j]<data[i][j+1] and data[i][j]<data[i-1][j] and data[i][j]<data[i+1][j]:
            out+=data[i][j]+1
print(out)