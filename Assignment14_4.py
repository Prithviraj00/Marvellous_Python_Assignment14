class Student:
    School_name = "ABC School"
    def __init__(self,A,B):
        self.name = A
        self.rollno = B



def main():
    obj1 = Student("Rahul",1)
    
    print("Name :",obj1.name )
    print("rollno :",obj1.rollno)
    print("School Name :",obj1.School_name)
    
    obj1.School_name = "New School"
    print("Changed School Name :",obj1.School_name)
    
    

if __name__ == "__main__":
    main()