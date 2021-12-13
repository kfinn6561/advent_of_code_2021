class Octopus():
    def __init__(self,n):
        self.counter=n
        self.flashing=False
        self.neighbours=[]
    
    def add(self):
        self.counter+=1
        if self.counter>9:
            if not self.flashing:
                self.flashing=True
                return True
        return False

    def flash(self):
        if self.flashing:
            self.counter=0
            self.flashing=False
            return 1
        return 0

with open('input.txt','r') as f:
    lines=f.readlines()

X=10
Y=10

octopi=[]
for line in lines:
    temp=[]
    for char in line.strip():
        temp.append(Octopus(int(char)))
    octopi.append(temp)

for i in range(X):
    for j in range(Y):
        nb=[]
        for x in range(max(i-1,0),min(i+2,X)):
            for y in range(max(j-1,0),min(j+2,Y)):
                if not(i==x and j==y):
                    nb.append(octopi[x][y])
        octopi[i][j].neighbours=nb

def step():
    out=0
    to_check=[]
    for i in range(X):
        for j in range(Y):
            to_check.append(octopi[i][j])
    while len(to_check)>0:
        octopus=to_check.pop(0)
        if octopus.add():
            to_check+=octopus.neighbours

    for i in range(X):
        for j in range(Y):
            out+=octopi[i][j].flash()
    return out

def print_op():
    for i in range(X):
        temp=''
        for j in range(Y):
            temp+=str(octopi[i][j].counter)
        print(temp)


s=1
while True:
    if step()==100:
        break
    s+=1

print(s)


    
