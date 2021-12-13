from collections import defaultdict
class Sheet():
    def __init__(self):
        self.x_dict=defaultdict(set)

    def add(self,x,y):
        self.x_dict[x].add(y)

    def fold_x(self,x_fold):
        out=Sheet()
        for x in self.x_dict.keys():
            for y in self.x_dict[x]:
                if x<x_fold:
                    out.add(x,y)
                else:
                    out.add(2*x_fold-x,y)
        return out

    def fold_y(self,y_fold):
        out=Sheet()
        for x in self.x_dict.keys():
            for y in self.x_dict[x]:
                if y<y_fold:
                    out.add(x,y)
                else:
                    out.add(x,2*y_fold-y)
        return out
    
    def count(self):
        out=0
        for x in self.x_dict.keys():
            for y in self.x_dict[x]:
                out+=1
        return out

    def print(self):
        max_y=max(set.union(*list(self.x_dict.values())))
        max_x=max(self.x_dict.keys())
        for y in range(max_y+1):
            temp=''
            for x in range(max_x+1):
                if y in self.x_dict[x]:
                    temp+='#'
                else:
                    temp+='.'
            print(temp)


with open('input.txt', 'r') as f:
    lines=f.readlines()

sheet=Sheet()
i=0
while lines[i].strip()!='':
    x,y=lines[i].split(',')
    sheet.add(int(x),int(y))
    i+=1

i+=1
while i<len(lines):
    dir,coord=lines[i].strip('fold along ').split('=')
    if dir.strip()=='x':
        sheet=sheet.fold_x(int(coord))
    elif dir.strip()=='y':
        sheet=sheet.fold_y(int(coord))
    else:
        print('unknown direction',dir)
    #print(sheet.count())
    i+=1

sheet.print()