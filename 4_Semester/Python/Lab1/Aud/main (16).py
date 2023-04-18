class YesInit:
    def __init__(self,one="noname",two="nonametoo"):
        self.fname = one; self.sname = two
obj1 = YesInit("Sasha","Tu");obj2 = YesInit()
obj3 = YesInit("Spartak"); obj4 = YesInit(two="Harry")
print (obj1.fname,obj1.sname); print (obj2.fname,obj2.sname)
print (obj3.fname,obj3.sname); print (obj4.fname, obj4.sname)
