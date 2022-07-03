import Food 

class ord:
    def __init__(self) -> None:
        self.lord=[]
        self.validpat=["chicken,","egg"]
        self.validsize=["small","large"]
        self.valistype=["shakes","fries"]
        self.menu="Burger-> Chicken and Egg patties \n Extras-> Fries and Shakes \n Size->large and small"
    def addburg(self,pat=None,size=None):
        if pat==None or size==None or not pat in self.validpat or not size in self.validsize:
            raise Exception("Invalid order2")
        burg =Food.Burger(pat,size)
        self.lord.append(burg)
    def addextra(self,type=None,size=None):
        if type==None or size==None or not type in self.validtype or not size in self.validsize:
            raise Exception("Invalid order3")
        ext=Food.Extras(type,size)
        self.lord.append(ext)
    def get_tot(self):
        if len(self.lord)==0:
            return 0
        tot=[v.get_price() for v in self.lord]
        return sum(tot)
    def get_menu(self):
        return self.menu
    def get_valid(self):
        return self.valid
oop=ord()
val=oop.get_menu()
print(val)