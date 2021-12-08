with open('input.txt','r') as f:
    lines=f.readlines()

program={
    'forward':0,
    'down':0,
    'up':0
}

for line in lines:
    instruction,amount=line.split()
    program[instruction]+=int(amount)

print(program['forward']*(program['down']-program['up']))