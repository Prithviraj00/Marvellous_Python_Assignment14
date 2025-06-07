class Person:
    def __init__(self,A,B):
        self.name = A
        self.age = B 

class Teacher(Person):
    def __init__(self,A,B,C,D):
        super().__init__(A,B)
        self.subject = C
        self.salary = D
        print("Name :",self.name) 
        print("Age :",self.age) 
        print("Subject :",self.subject) 
        print("salary :",self.salary) 
            
def main():
    obj1 = Teacher("Niranjan",23,"Maths",80000)

if __name__ == "__main__":
    main()