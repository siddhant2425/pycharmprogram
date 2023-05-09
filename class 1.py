

class student:
    course='python'#class variable
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
    def show(self):
        print("id is::",self.id)
        print("Name is::",self.name)
        print("salary is::",self.sal)
        print("course Name::",student.course)
        print("Collage Name::",student.collage)
    def add(self,a,b):
        self.a=a
        self.b=b
        c=self.a+self.b
        print(c)




st1 =student(101,'Siddhant',45000)

student.collage="YC"#outside class variable
st1.show()
st1.add(12,56)


