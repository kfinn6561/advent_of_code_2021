with open('input.txt','r') as f:
    lines=f.readlines()

brace_pairs={
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}
braces=list(brace_pairs.keys())+list(brace_pairs.values())

scores={
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}

def find_corrupted(line):
    to_close=[]
    next_close='+'#dummy
    for char in line:
        if char not in braces: #probably won't happen, but could be code inside braces?
            continue
        if char in brace_pairs.keys():
            to_close.append(next_close)
            next_close=brace_pairs[char]
        else:
            if char==next_close:
                next_close=to_close.pop()
            else:
                return scores[char]
    return 0

count=0
for line in lines:
    count+=find_corrupted(line)

print(count)