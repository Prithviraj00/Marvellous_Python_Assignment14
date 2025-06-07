class Vehicle   :
    def start(self):
        print("Vehicle Start")

class Car(Vehicle):
    def start(self):
        print("Car Start")
        
def main():
    obj1 = Car()
    obj1.start()

if __name__ == "__main__":
    main()