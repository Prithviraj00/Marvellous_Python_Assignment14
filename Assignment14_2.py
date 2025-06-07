class Rectangle:
    def __init__(self,A,B):
        self.length = A
        self.width = B
        
    def Area(self):
        Ans = self.width * self.length
        print("Area :",Ans)
    
    def perimeter(self):
        Ans = 2 *(self.length + self.width)
        print("Perimeter :",Ans)
    
def main():
        obj1= Rectangle (10,5)
        obj1.Area()
        obj1.perimeter()
        
if __name__ == "__main__":
    main()