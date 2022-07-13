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
        if self.pat=="None":
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
        if self.patties=="shakes":
            base_price+=(3*self.sprice[self.size])
        return base_price
