from Order import ord

class cntroler:
    def __init__(self) -> None:
        self.order=ord()
        print("Hello")
    def get_menu(self):
        return self.order.get_menu()

    def add_order(self,st):
        ors=st.split(",")
        format=[v.split(" ") for v in ors]
        for v in format:
            if len(v)!=4:
                raise Exception("Invalid order")
            if  not v.isdigit():
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
oos=cntroler()
val=oos.get_menu()
print(val)