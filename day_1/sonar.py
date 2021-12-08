with open('input.txt','r') as f:
    lines=f.readlines()

out=0
for i in range(1,len(lines)):
    if int(lines[i])>int(lines[i-1]):
        out+=1
print(out)