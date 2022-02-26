class computer:
    def __init__(self):
        self.name="suyash"
        self.age="24"
    
    
         
    

    def compare(self,c2):
        if self.age==c2.age:
            return True
        else:
            print("false")
        



c1=computer()
c2=computer()
c1.age=44

if c1.compare(c2):
    print("they are same")
else:
    print("false")
              

        