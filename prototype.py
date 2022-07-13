from abc import ABCMeta, abstractmethod
import copy

class Books_at_Leddy_Library(metaclass = ABCMeta):
  
  # constructor
  def __init__(self):
    self.id = None
    self.type = None

  @abstractmethod
  def book_details(self):
    pass

  def get_type(self):
    return self.type

  def get_id(self):
    return self.id

  def set_id(self, sid):
    self.id = sid

  def clone(self):
    return copy.copy(self)

class Book1(Books_at_Leddy_Library):
  def __init__(self):
    super().__init__()
    self.type = "This is Book 1"

  def book_details(self):
    print("Inside Book1::book_details() method.")

class Book3(Books_at_Leddy_Library):
  def __init__(self):
    super().__init__()
    self.type = "This is Book 3"

  def book_details(self):
    print("Inside Book3::book_details() method.")

class Book2(Books_at_Leddy_Library):
  def __init__(self):
    super().__init__()
    self.type = "This is Book 2"

  def book_details(self):
    print("Inside Book2::book_details() method.")

class Books_at_Leddy_Library_Cache:
  cache = {}

  @staticmethod
  def get_books(sid):
    book_base = Books_at_Leddy_Library_Cache.cache.get(sid, None)
    return book_base.clone()

  @staticmethod
  def load():
    b3 = Book3()
    b3.set_id("1")
    Books_at_Leddy_Library_Cache.cache[b3.get_id()] = b3

    b1 = Book1()
    b1.set_id("2")
    Books_at_Leddy_Library_Cache.cache[b1.get_id()] = b1

    b2 = Book2()
    b2.set_id("3")
    Books_at_Leddy_Library_Cache.cache[b2.get_id()] = b2

# main function
if __name__ == '__main__':
  Books_at_Leddy_Library_Cache.load()

  b3 = Books_at_Leddy_Library_Cache.get_books("3")
  print(b3.get_type())
  print(b3.book_details())

  b1 = Books_at_Leddy_Library_Cache.get_books("1")
  print(b1.get_type())
  print(b1.book_details())

  b2 = Books_at_Leddy_Library_Cache.get_books("2")
  print(b2.get_type())
  print(b2.book_details())