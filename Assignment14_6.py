class Calculator:
    def __init__(self,A,B):
        self.value1 = A
        self.value2 = B 

    def add(self):
        ans = self.value1 + self.value2
        print("add is :",ans)
        
    def subtract(self):
        ans = self.value1 - self.value2
        print("subtract is :",ans)
    
    def multiply(self):
        ans = self.value1 * self.value2
        print("multiply is :",ans)

    def division(self):
        ans = self.value1 / self.value2
        print("division is :",ans)
        
def main():
    print("Enter ur first number:")
    value1 = int(input())
    
    print("Enter ur second number:")
    value2 = int(input())
    
    obj1 = Calculator(value1,value2)
    obj1.add()
    obj1.subtract()
    obj1.multiply()
    obj1.division()

if __name__ == "__main__":
    main()