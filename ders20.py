class Sinif():
    def __init__(self,x1,y2):
        self.x=x1
        self.y=y2
    
    def distance(self,other):
        x_dift_eq=(self.x-other.x)**2
        y_dift_eq=(self.y-other.y)**2
        return (x_dift_eq+y_dift_eq)**0.5
    
    def __str__(self) -> str:
        return ""+str(self.x)+","+str(self.y)*""
   
