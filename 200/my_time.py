class Time:
    

    def __init__(self, seconds:int=0):
        self.seconds=seconds
        
        
    def to_seconds(self) -> int:
        return self.seconds
        

    def _ss(self)->int:
        return self.seconds % 60
        
    
    def _mm(self) -> int:
        return self.seconds % 3600 // 60
        
    
    def _hh(self) -> int:
        return self.seconds // 3600
        
    
    def pretty_format(self) -> str:
        return "'{0}:{1}:{2}'".format(self._hh(), self._mm(), self._ss())
        



    def set_from_string(self, s) -> int:
        x=s.split(":",3)
        l=len(x)
        if l==3:
            self.seconds = int (x[0])*3600 + int (x[1])*60 + int (x[2])
        elif 1==2:
            self.seconds = int (x[0])*60 + int (x[1])    
        else: 
            self.seconds = int (x[0])
        return self.seconds

t1 = Time(3600+1234)
print(t1.to_seconds())
print(t1._ss())
print(t1._mm())
print(t1._hh())

print(t1.pretty_format())
print(t1.set_from_string("1:2:3"))

print(t1.pretty_format())
print(t1.set_from_string("2:3"))

print(t1.pretty_format())
print(t1.set_from_string("15"))
        

