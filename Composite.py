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
    def __init__(self,col) -> None:
        super().__init__()
        self.color=col
    def operation(self,col):
        self.color=col
        print("a book color changed")

class library(component):
    def __init__(self) -> None:
        super().__init__()
        self.children=[]
    def add_children(self, child):
        self.children.append(child)
        print("Added book "+child.color)
    def operation(self,col):
        for i,v in enumerate(self.children):
            b_color=v.color
            v.operation(col)
            print(b_color+" book  has updated color: "+v.color)
        print("library operation done means its compositional children operation is done ")
print("How many books do you wanna add:")
n=input()
list_books=[ ]
for i in range(int(n)):
    print("mention color of book:")
    st=input()
    list_books.append(book(st))
lib=library()
for val in list_books:
    lib.add_children(val)
print("Press 1 to change color essesnce of library:")
n=input()
if n=="1":
    print('Add the color of  the librarys essence:')
    col=input()
    lib.operation(col)
3







    