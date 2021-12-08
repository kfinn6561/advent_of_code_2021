with open('input.txt','r') as f:
    lines=f.readlines()
count=0
for line in lines:
    decypher=line.split('|')[1].split()
    for char in decypher:
        if len(char.strip()) in [2,4,3,7]:
            count+=1
    
print(count)