

class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name is::",self.name)
        print("Age is::",self.age)
class B(A):
    def __init__(self,name,age,id,salary):
        super().__init__(name,age)
        self.id=id
        self.salary=salary
    def show(self):
        super().show()
        print("id is::",self.id)
        print("salary is::",self.salary)

obj=B('siddhant',25,101,75000)
obj.show()