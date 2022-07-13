class pressbeans:
    @staticmethod
    def method():
        return "pressed bean "
class addwater:
    @staticmethod
    def method():
        return "added water "
class fiter:
    @staticmethod
    def method():
        return "filterd coffee"

class make_coffee:
    def __init__(self) -> None:
        self.a=pressbeans()
        self.b=addwater()
        self.c=fiter()
    def create(self):
        res=self.a.method()+self.b.method()+self.c.method()
        print(res)
        print("coffee made!!!")

print("Press 1 to make coffee")
n=input()    
if n=="1":
    coffee_maker=make_coffee()
    coffee_maker.create()