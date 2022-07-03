from Controller import cntroler
class Ui:
    def __init__(self) -> None:
        self.cont= cntroler()
        
    def display(self):
        while(1):
            print("Press 1 to see menu , 2 to see total price of order, or place order")
            inp=input()
            if len(inp)==1 and inp=="1":
                self.cont.get_menu()
            if len(inp)==1 and inp=="2":
                print("Total is ",self.cont.get_tot())
            else:
                self.cont.add_order(inp)


ui=Ui()
ui.display()