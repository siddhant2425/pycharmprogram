
class A():
    pass
    # def m1(self):
    #     print("from m1 A")
class B():
    def m1(self):

        print("from m2 B")
class C(A,B):
    def m1(self):

        super().m1()
        print("from m3 C")


obj=C()
obj.m1()