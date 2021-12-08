with open('input.txt','r') as f:
    lines=f.readlines()

def bin_to_dec(bin):
    out=0
    for i in range(len(bin)):
        j=len(bin)-i-1
        out+=bin[i]*(2**j)
    return out

N_readings=len(lines)
N_bits=len(lines[0].strip())

sums=[0]*N_bits
for line in lines:
    for i in range(N_bits):
        sums[i]+=float(line[i])

gamma=[]
epsilon=[]
for i in range(N_bits):
    if sums[i]/N_readings>0.5:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

print(bin_to_dec(gamma)*bin_to_dec(epsilon))