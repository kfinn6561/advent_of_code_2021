from collections import defaultdict
with open('input.txt','r') as f:
    lines=f.readlines()

template=lines[0].strip()

rules={}
for line in lines[2:]:
    a,b=line.split('->')
    rules[a.strip()]=b.strip()


def step(polymer):
    out=''
    for i in range(len(polymer)-1):
        test=polymer[i:i+2]
        out+=test[0]
        if test in rules.keys():
            out+=rules[test]
    out+=polymer[-1]
    return out

for _ in range(40):
    template=step(template)

count=defaultdict(int)
for char in template:
    count[char]+=1
print(max(count.values())-min(count.values()))