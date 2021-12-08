letters=['a','b','c','d','e','f','g']

wires_to_n={
    'abcefg':0,
    'cf':1,
    'acdeg':2,
    'acdfg':3,
    'bcdf':4,
    'abdfg':5,
    'abdefg':6,
    'acf':7,
    'abcdefg':8,
    'abcdfg':9
}

def get_by_length(digits,length):
    for digit in digits:
        if len(digit)==length:
            return digit

def crack_code(digits):
    known={}
    for letter in letters:
        count=0
        for digit in digits:
            if letter in digit:
                count+=1
        if count==4:
            known['e']=letter
        if count==6:
            known['b']=letter
        if count==9:
            known['f']=letter
    one=get_by_length(digits,2)
    for char in one:
        if char!=known['f']:
            known['c']=char
    seven=get_by_length(digits,3)
    for char in seven:
        if char not in [known['f'],known['c']]:
            known['a']=char
    four=get_by_length(digits,4)
    for char in four:
        if char not in [known['b'],known['c'],known['f']]:
            known['d']=char
    for letter in letters:
        if letter not in known.values():
            known['g']=letter
    return dict((v,k) for k,v in known.items())

def read_digit(digit,decoder):
    decoded=[]
    for char in digit:
        decoded.append(decoder[char])
    return wires_to_n[''.join(sorted(decoded))]

def decode(digits,decoder):
    out=0
    for i in range(len(digits)):
        out+=read_digit(digits[i],decoder)*(10**(len(digits)-1-i))
    return out

with open('input.txt','r') as f:
    lines=f.readlines()

count=0
for line in lines:
    coded,to_decode=line.split('|')
    decoder=crack_code(coded.split())
    count+=decode(to_decode.split(),decoder)
print(count)
