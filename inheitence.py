class square:
    def __init__(self):
        self.x=x
    def area(self):
        print("area of square is ",self.x*self.x)
class rectangle:
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def area(self):
        super.area()
        print("area of square is ",self.x*self.y)
a,b=map(float,input("enter two no\'s: ").split())
r=rectangle(a,b)
r.area()