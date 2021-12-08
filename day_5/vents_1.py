from collections import defaultdict

def read_point(point):
    x,y=point.split(',')
    return int(x),int(y)

def read_line(line):
    p1,p2=line.split('->')
    x1,y1=read_point(p1)
    x2,y2=read_point(p2)
    return x1,y1,x2,y2

squares=defaultdict(int)

with open('input.txt','r') as f:
    lines=f.readlines()

for line in lines:
    x1,y1,x2,y2=read_line(line)
    if x1==x2:
        for y in range(min(y1,y2),max(y1,y2)+1):
            squares[(x1,y)]+=1
    elif y1==y2:
        for x in range(min(x1,x2),max(x1,x2)+1):
            squares[(x,y1)]+=1
out=0
for v in squares.values():
    if v>=2:
        out+=1
print(out)