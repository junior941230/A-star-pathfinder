import csv
import math
class A_star():
    def __init__(self):  
        self.closed_node = []
        self.open_node =[]
        self.came_from = {}
        self.g_scole ={}
        self.h_score= {}
        self.f_score = {}
        self.out = []

    def neighbor(self,p,data):
        for i in data:
            if p == i[0]:
                find = i
                return find

    def Mandis(self,p1,p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p1[1])
    
    def dis(self,p1,p2):
        return math.dist(p1,p2)

    def min_f(self,p1):
        temp = 10000
        for i in self.open_node:
            if self.Mandis(p1,i) < temp:
                temp = self.Mandis(p1,i)
                temppoint = i  
        return temppoint
    
    def calculate(self,startpoint,endpoint,data):
        self.open_node.append(startpoint)
        self.g_scole[startpoint] = 0  
        self.h_score[startpoint] = self.Mandis(startpoint,endpoint)
        self.f_score[startpoint] = self.h_score[startpoint]
        while len(self.open_node)>0:
            self.x = self.min_f(self.open_node[0])
            if self.x == endpoint:
                out = self.output(self.x)
                for i in range(int(len(out)/2)):
                    self.out.append((out[i*2],out[i*2+1]))
                return self.out
            self.open_node.remove(self.x)
            self.closed_node.append(self.x)
    
            for y in self.neighbor(self.x,data):
                if y in self.closed_node:
                    continue
                
                temp_g_score = self.g_scole[self.x] + self.dis(self.x,y)
                if y not in self.open_node:
                    temp_better = True
                elif temp_g_score < self.g_scole[y]:
                    temp_better = True
                else:
                    temp_better = False
                if temp_better == True:
                    self.came_from[y] = self.x
                    self.g_scole[y] = temp_g_score
                    self.h_score[y] = self.Mandis(y,endpoint)
                    self.f_score[y] = self.g_scole[y] + self.h_score[y]
                    self.open_node.append(y)
        return "fail"


    def output(self,current):
        if self.came_from.get(current)!= None:
            p = self.output(self.came_from[current])
            return p + current
        else:
            return current

with open('path.csv', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=':')  
    pathdata =[]
    for r in rows:
        pointrowdata = []
        for i in r[0].split(","):
            pointrowdata.append(i)
        pathdata.append(pointrowdata)

with open('point.csv', newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=':')
    pointdata =[]
    for r in rows:
        pointdata.append((int(r[0].split(",")[0]),int(r[0].split(",")[1])))

data = []
for i in range(len(pathdata)):
    rowdata = []
    for a in pathdata[i]:
        rowdata.append(pointdata[int(a)-1])
    data.append(rowdata)

print(A_star().calculate((354,35),(51,34),data))