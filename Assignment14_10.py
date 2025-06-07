class Employee:

    def __init__(self,A,B,C):
        self.name = A
        self._department = B
        self.__salary = C
        
    def display(self):
        print("Employee Name :",self.name)
        print("Employee department :",self._department)
        print("Employee salary :",self.__salary)

def main():
    obj1= Employee("Rahul","Maths",1000)
    obj1.display()
    print("Employee Name :",obj1.name)
    print("Employee department :",obj1._department)
    print("Employee salary :",obj1.__salary)
    
    

if __name__ == "__main__":
    main()