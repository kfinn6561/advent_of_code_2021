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

readings=[]
for line in lines:
    temp=[]
    for i in range(N_bits):
        temp.append(int(line[i]))
    readings.append(temp)

def most_common(data,position):
    total=0
    for datum in data:
        total+=datum[position]
    return int(total>=len(data)/2)

def get_rating(rdngs,mc):
    i=0
    while len(rdngs)>1:
        digit=most_common(rdngs,i)
        if not mc:
            digit=(digit+1)%2
        temp=[]
        for r in rdngs:
            if r[i]==digit:
                temp.append(r)
        rdngs=temp
        i+=1
    return bin_to_dec(rdngs[0])


ogr=get_rating(readings,True)
csr=get_rating(readings,False)

print(ogr*csr)
