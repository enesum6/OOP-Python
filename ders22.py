class Employe:
    def __init__(self,firstname,lastname,pay):
        self.firstname=firstname
        self.lastname=lastname
        self.email=firstname+"."+lastname+"@company.com"
        self.pay=pay
    
    def fullname(self):
        return "{}{}".format(self.firstname,self.lastname)
    
    def apply_raise(self):
        self.pay=int(self.pay*1.04)
        
    def __len__(self):
        return len(self.fullname())
emp1=Employe("Enes","Menal",50000)
emp2=Employe("Test","User",60000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(len(emp1))
print(len(emp2))