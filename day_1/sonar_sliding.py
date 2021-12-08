with open('input.txt','r') as f:
    lines=f.readlines()
measurements=[int(line) for line in lines]

out=0
slide=sum(measurements[:3])
for i in range(3,len(measurements)):
    new=slide+measurements[i]-measurements[i-3]
    if new>slide:
        out+=1
    slide=new
print(out)