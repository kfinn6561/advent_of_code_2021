from collections import defaultdict
with open('input.txt','r') as f:
    lines=f.readlines()

template=lines[0].strip()

rules={}
for line in lines[2:]:
    a,b=line.split('->')
    rules[a.strip()]=b.strip()

pairs=defaultdict(int)
for i in range(len(template)-1):
    pairs[template[i:i+2]]+=1


def step(input_pairs):
    out=defaultdict(int)
    for pair in input_pairs.keys():
        if pair in rules.keys():
            p1=pair[0]+rules[pair]
            p2=rules[pair]+pair[1]
            out[p1]+=input_pairs[pair]
            out[p2]+=input_pairs[pair]
        else:
            out[pair]+=input_pairs[pair]
    return out

for _ in range(40):
    pairs=step(pairs)

count=defaultdict(int)
for pair in pairs.keys():
    count[pair[0]]+=pairs[pair]
count[template[-1]]+=1#the last letter won't be counted in the above
print(max(count.values())-min(count.values()))