class Employe:
    def __init__(self,firstname,lastname,pay):
        self.firstname=firstname
        self.lastname=lastname
        self.email=firstname+"."+lastname+"@company.com"
        self.pay=pay
    
    def fullname(self):
        return "{}{}".format(self.firstname,self.lastname)

emp1=Employe("Enes","Menal",50000)
emp2=Employe("Test","User",60000)
#print(emp1)
#print(emp2)



print(emp1.email)
print(emp2.email)
print("{}{}".format(emp1.firstname,emp1.lastname))  #EnesMenal
print(emp1.fullname())                              #EnesMenal
print(Employe.fullname(emp1))                       #EnesMenal