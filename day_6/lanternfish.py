
fish=[0 for i in range(9)]

def read_input(fname):
    with open(fname,'r') as f:
        r=f.read()
    new_fish=r.split(',')
    for nf in new_fish:
        i=int(nf)
        fish[i]+=1

def step():
    births=fish.pop(0)
    fish[6]+=births
    fish.append(births)

if __name__ =='__main__':
    read_input('input.txt')
    for i in range(256):
        step()
    print(sum(fish))