

class A:
    def m1(self):
        print("From m1")

class B():
    def m2(self):
        print("from m2")
class C(B,A):
    def m3(self):
        print("From M3")

obj=C()
obj.m3()
obj.m1()
obj.m2()
