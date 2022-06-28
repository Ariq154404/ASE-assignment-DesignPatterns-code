from abc import ABCMeta, abstractmethod
class interfaceA(metaclass=ABCMeta):
    @abstractmethod
    def send_string(self):
        pass
        
class interfaceB(metaclass=ABCMeta):
     @abstractmethod
     def send_list(self):
         pass
class typeA(interfaceA):
    def send_string(self,sample):
        print("value sent in string",sample)
        return sample
class typeB(interfaceB):
    def send_list(self,sample):
        print("value sent in list",sample)
        return sample
class Adapter(interfaceA):
    def __init__(self) -> None:
        super().__init__()
        self.B=typeB()
    def send_string(self,sample):
        sample=sample.split()
        sample= self.B.send_list(sample)
        return sample
def client(adapter):
    print("Client sends string but dosent have to worry about the format")
    val=adapter.send_string("1 2 3")
    return val
ada=Adapter()
server=client(ada)
print("server receivers",server)


