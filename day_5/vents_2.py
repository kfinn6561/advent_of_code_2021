from collections import defaultdict

def read_point(point):
    x,y=point.split(',')
    return int(x),int(y)

def read_line(line):
    p1,p2=line.split('->')
    x1,y1=read_point(p1)
    x2,y2=read_point(p2)
    return x1,y1,x2,y2

sign = lambda a: (a>0) - (a<0)


squares=defaultdict(int)

with open('input.txt','r') as f:
    lines=f.readlines()

for line in lines:
    x1,y1,x2,y2=read_line(line)
    x_dir=sign(x2-x1)
    y_dir=sign(y2-y1)
    mag=max(abs(y2-y1),abs(x2-x1))
    for i in range(mag+1):
        x=x1+i*x_dir
        y=y1+i*y_dir
        squares[(x,y)]+=1
        
out=0
for v in squares.values():
    if v>=2:
        out+=1
print(out)