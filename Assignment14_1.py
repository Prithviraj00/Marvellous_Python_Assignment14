class Employee:
    def __init__(self,Name,ID,Salary):
        self.name = Name
        self.emp_id = ID
        self.salary = Salary
        
    def Display(self):
        print("Name :",self.name)
        print("ID :",self.emp_id)
        print("Salary :",self.salary)

def main():
    emp1 = Employee('Shubham',101,'50000')
    emp2 = Employee('Vicky',102,'80000')
    
    emp1.Display()
    emp2.Display()

if __name__ == "__main__":
    main()