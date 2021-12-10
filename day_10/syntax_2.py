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
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

def find_incomplete(line):
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
                return 0
    to_close.append(next_close)
    if '+' in to_close:
        to_close.remove('+')
    out=0
    for brace in to_close[::-1]:
        out*=5
        out+=scores[brace]
    return out





line_scores=[]
for line in lines:
    score=find_incomplete(line)
    if score!=0:
        line_scores.append(score)
line_scores.sort()
i=int(len(line_scores)/2)

print(line_scores[i])