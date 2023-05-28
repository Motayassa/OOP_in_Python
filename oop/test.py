class Test:
    z=12
    i=56
    def set_value(self,x,y):
        self.x=x
        self.y=y
    def display(self):
        return (self.x,self.y)
o=Test()
print(Test.z)
o.set_value(40,100)
print(o.display())