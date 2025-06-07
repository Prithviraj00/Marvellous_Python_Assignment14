class Book:
    def __init__(self,A,B):
        self.Name = A
        self.__price = B
    
    def get(self):
        return self.__price
    
    def set(self,value):
        self.__price = value
    
def main():
    obj1 = Book("Ramayan",10000)
    print("Book Name",obj1.Name)
    print("Book Price",obj1.get())
    print("Book Price",obj1.set(500))
    print("Book Price",obj1.get())
  #  print("Book Price",obj1.__price)     #You can not Access Private variables.
    
    
    
    
    

if __name__ == "__main__":
    main()