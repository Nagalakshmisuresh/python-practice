class fruits:
    def read(self):
        self.name=input("name")
        self.cost=int(input("Enter cost"))
    def display(self):
        print(self.name,self.cost)
f1=fruits()
f1.read()
f1.display()
        