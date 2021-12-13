from collections import defaultdict
data=defaultdict(list)

with open('input.txt','r') as f:
    lines=f.readlines()
for line in lines:
    a,b=line.split('-')
    a=a.strip()
    b=b.strip()
    data[a].append(b)
    data[b].append(a)

paths=[['start']]
finished=[]

while len(paths)>0:
    path=paths.pop(0)
    for next in data[path[-1]]:
        p=path+[next]
        if next=='end':
            finished.append(p)
        elif next[0].isupper():
            paths.append(p)
        else:
            if next not in path:
                paths.append(p)

print(len(finished))