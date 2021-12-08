with open('input.txt','r') as f:
    lines=f.readlines()

program={
    'forward':0,
    'down':0,
    'up':0
}
depth=0

def aim():
    return program['down']-program['up']

for line in lines:
    instruction,amount=line.split()
    if instruction=='forward':
        depth+=int(amount)*aim()
    program[instruction]+=int(amount)

print(program['forward']*depth)