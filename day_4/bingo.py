import sys 

class Board():
    def __init__(self,text):
        text=text.strip()
        lines=text.split('\n')
        self.numbers=[]
        for line in lines:
            temp=[]
            for number in line.strip().split():
                temp.append(int(number))
            self.numbers.append(temp)
        self.N=len(self.numbers)
        self.M=len(self.numbers[0])
        self.marked=[[0]*self.M for _ in range(self.N)]

    def mark(self,n):
        changed=False
        for i in range(self.N):
            for j in range(self.M):
                if self.numbers[i][j]==n:
                    changed=True
                    self.marked[i][j]=1
        if changed:
            return self.check_for_win()
        else:
            return False

    def check_for_win(self):
        for i in range(self.N):
            if sum(self.marked[i])==self.M:
                return True
        for j in range (self.M):
            if sum([self.marked[i][j] for i in range(self.N)])==self.N:
                return True
        return False

    def sum_unmarked(self):
        out=0
        for i in range(self.N):
            for j in range(self.M):
                out+=self.numbers[i][j]*((self.marked[i][j]+1)%2)
        return out

def parse_input(fname):
    with open(fname,'r') as f:
        text=f.read()
    lines=text.split('\n\n')
    numbers=[int(x) for x in lines[0].split(',')]
    boards=[Board(t) for t in lines[1:]]
    return numbers,boards

numbers,boards=parse_input('input.txt')

for number in numbers:
    for board in boards:
        if board.mark(number):
            print(board.sum_unmarked()*number)
            sys.exit()