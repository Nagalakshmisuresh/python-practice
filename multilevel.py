class A:
    def m1(self):
        print("dhoni")
class B(A):
    def m2(self):
        print("raina")
    def m1(self):
        print("bravo")
class C(B):
    def m3(self):
        print("csk")
obj=C()
obj.m1()
obj.m3()
obj.m2()