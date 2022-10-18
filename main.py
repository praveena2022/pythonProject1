class father:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
f=father()
f.setname("madhayappa")
print("father= ",f.getname())
class daughter(father):
    def setn1(self,n1):
        self.n1=n1
    def getn1(self):
        return self.n1
d=daughter()
d.setname("madhayappa")
d.setn1("lavanya")
print("father\' s nmae is  ",d.getname())
print("daughter\'s name is  ",d.getn1())


class pop:
    def __init__(self):
        self.property= 10000000
    def display_property(self):
        print("father\'s property is ",self.property)
    def setname(self,name):
        self.name="lavanya"
    def getname(self):
        return self.name

class son(pop):
    def __init__(self):
        self.property= 500000
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def display_property(self):
        print("father\'s property is ",self.property)


s=son()
s.setname('laddu')
print("nmae is ",s.getname())
s.display_property()