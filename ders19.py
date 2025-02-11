class Circle():
    def __init__(self,radius):
        """Initializae self with radius"""
        self.r=radius
    def get_radius(self):
        """Return the radius of self"""
        return self.r
    def set_radius(self,radius):
        self.r=radius

    def get_area(self):
        """Return the area of self using p1=3.14"""
        return 3.14*self.r*self.r
    
    def equal(self,c):
        """C is a circle object
        Return true if self and c have the same radius value"""
        return (c.r==self.r)
    def bigger(self,c):
        """c is a circle object
        Returns self or c, the circle object with the bigger radius"""
        if(c.r>self.r):
            return c
        elif(c.r<self.r):
            return self
        
  
c1=Circle(1)
c2=Circle(2)
print(c2.get_area())
print(c1.get_area())
c3=c1.bigger(c2)
print(c3.get_radius())
print(c2.get_radius())

