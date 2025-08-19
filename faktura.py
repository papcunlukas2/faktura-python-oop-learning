import invoice27x


class Person:
    """
    Person - a class that describes a person
    """
    def __init__(self, __id: int, name: str, email: str, male: bool):
        self.name = name
        self.email = email
        self.male = male
        self.__id = __id
        print(f"{name} was born.")

    def __str__(self):
        return f"Hello, my name is {self.name}."
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id


class Customer(Person):
    def __init__(self, __id: int, name: str, email: str, male: bool, balance: int = 0):
        super().__init__(__id, name, email, male)
        self.balance: int = balance
        print(f"{name} is a new customer.")
    
    def __str__(self) -> str:
        return f"Hello, I have {self.balance} balance."
    
    def nespokojny():
        print("Chcem rozpravat z managerom.")


class Order:
    def __init__(self, item: str, quantity: int, pricePerUnit: int):
        self.item: str = item
        self.quantity: int = quantity
        self.pricePerUnit: int = pricePerUnit

    def thisPrice(self) -> int:
        return self.quantity * self.pricePerUnit
        

class Administrator(Person):
    def __init__(self, __id: int, name: str, email: str, male: bool):
        super().__init__(__id, name, email, male)
        self.managedInvoices: list = []
        print(f"{name} is a new admin.")
    
    def __str__(self) -> str:
        return f"Hello, I have {self.balance} balance."
    
    def assignInvoice(self, invoice: invoice27x.Invoice):
        self.managedInvoices.append(invoice)
        print(f"Invoice {invoice.__id} assigned to: {self.name}")


if __name__ == "__main__":
    customer1: Customer = Customer(0, "Jozko", "test@jozko.com", True, 5000)
    admin1: Administrator = Administrator(1, "Random", "random@random.xyz", False)
    invoice1: invoice27x.Invoice = invoice27x.Invoice(customer1, admin1)
