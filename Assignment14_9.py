class Product:

    def __init__(self,A,B):
        self.name = A
        self.price = B
    def __eq__(self, value):
        return self.price == value.price
        


def main():
    obj1= Product("ABC",100)
    obj2= Product("XYZ",100)
    print(obj1 == obj2)

if __name__ == "__main__":
    main()