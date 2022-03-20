class Student:
    def __init__(self,name,phy,chm,bio):
        self.name,self.phy,self.chm,self.bio = name,phy,chm,bio
        
    def Total(self):
        return self.phy+self.chm+self.bio
    
    def percentage(self):
        return (Student.Total(self) / 300) * 100
name=str(input("your name :"))
phy=int(input("your phy marks:"))
chem=int(input("your chem marks: "))
bio=int(input("your bio marks : "))   
std = Student(name,phy,chem,bio)

print("your total marks",std.Total())
print("your percentage score ",std.percentage())