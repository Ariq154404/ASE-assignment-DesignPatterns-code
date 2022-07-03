from abc import ABCMeta, abstractmethod
class edible(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.sprice={"small":1,"large":2}
        pass
    @abstractmethod
    def get_price(self):
        pass
class Burger(edible):
    def __init__(self,pat=None,size=None) -> None:
        super().__init__()
        self.patties=pat
        self.size=size
    def get_price(self):
        if self.patties=="None":
            return 0
        base_price=10
        if self.patties=="chicken":
            base_price+=(12*self.sprice[self.size])
        if self.patties=="egg":
            base_price+=(5*self.sprice[self.size])
        return base_price
        
class Extras(edible):
    def __init__(self,type=None,size=None) -> None:
        super().__init__()
        self.type=type
        self.size=size
    def get_price(self):
        if self.type=="None":
            return 0
        base_price=1
        if self.type=="fries":
            base_price+=(2*self.sprice[self.size])
        if self.type=="shakes":
            base_price+=(3*self.sprice[self.size])
        return base_price




class ord:
    def __init__(self) -> None:
        self.lord=[]
        self.validpat=["chicken","egg"]
        self.validsize=["small","large"]
        self.validtype=["shakes","fries"]
        self.menu="Burger-> Chicken and Egg patties \n Extras-> Fries and Shakes \n Size->large and small"
    def addburg(self,pat=None,size=None):
        # print(pat,size,not (pat in self.validpat),not (size in self.validsize))
        if pat==None or size==None or not (pat in self.validpat) or not (size in self.validsize):
            raise Exception("Invalid order2")
        burg =Burger(pat,size)
        self.lord.append(burg)
    def addextra(self,type=None,size=None):
        # print(type, size)
        if type==None or size==None or not type in self.validtype or not (size in self.validsize):
            raise Exception("Invalid order3")
        ext=Extras(type,size)
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




class cntroler:
    def __init__(self) -> None:
        self.order=ord()
        # print("Hello")
    def get_menu(self):
        return self.order.get_menu()

    def add_order(self,st):
        ors=st.split(",")
        format=[v.strip().split(" ") for v in ors]
        for v in format:
            if len(v)!=4:
                raise Exception("Invalid order")
            if  not v[0].isdigit():
                raise Exception("Invalid order0")
            num=int(v[0])
            for c in range(num):
                if v[1]=="burger":
                    self.order.addburg(v[2],v[3])
                elif v[1]=="extras":
                    self.order.addextra(v[2],v[3])
                else:
                    raise Exception("Invalid Order55")
    def get_tot(self):
        return self.order.get_tot()



class Ui:
    def __init__(self) -> None:
        self.cont= cntroler()
        
    def display(self):
        while(1):
            print("Press 1 to see menu , 2 to see total price of order, or place order")
            inp=input()
            # print(inp)
            if len(inp)==1 and inp=="1":
                # print("hello")
                print(self.cont.get_menu())
            elif len(inp)==1 and inp=="2":
                print("Total is ",self.cont.get_tot())
            else:
                self.cont.add_order(inp)


ui=Ui()
ui.display()