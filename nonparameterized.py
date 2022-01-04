class college:
    def __init__(self,cn,cb,cid,cg):
        self.cname=cn
        self.cbranches=cb
        self.cid=cid
        self.cground=cg
    def display(self):
        print(self.cname,self.cbranches,self.cid,self.cground)
cg1=college("vkr","mechanical,civil",1,5)
cg1.display()
