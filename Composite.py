from abc import ABCMeta, abstractmethod

class component(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.children=None
        pass

    def add_children(self,chid):
        pass
    def operation(self):
        pass
        

class book(component):
    def __init__(self) -> None:
        super().__init__()
    def operation(self):
        print("a book operation done")

class library(component):
    def __init__(self) -> None:
        super().__init__()
        self.children=[]
    def add_children(self, child):
        self.children.append(child)
        print("Added book")
    def operation(self):
        for v in self.children:
            v.operation(self)
        print("library operation done after its children")
v=book()
list_books=[ book() for i in range(5)]
lib=library()
for val in list_books:
    lib.add_children(book)

lib.operation()






    