class Graph:
    LIMIT_Y = list(range(0, 11))
 

    def set_data(self,data):
        setattr(self, 'data', data) # просто переменная data для хранения списка
        
        
    def draw(self):
        res=[]
        for i in self.data:
            if i in Graph.LIMIT_Y:
                res.append(i)
        return res      
        
        
graph_1=Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])   
print(*graph_1.draw())