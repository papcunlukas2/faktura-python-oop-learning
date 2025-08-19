from faktura import Administrator, Customer, Order


class Invoice:
    __all_invoices = 0

    def __init__(self, customer: Customer, manager: Administrator, orders: list[Order] = []):
        Invoice.__all_invoices += 1
        self.__id = Invoice.__all_invoices
        self.customer = customer
        self.orders = orders
        self.approved = False
        manager.managedInvoices.append(self)

    def addOrder(self, order: Order):
        self.orders.append(order)

    def getTotal(self):
        total = 0
        for order in self.orders:
            total += order.thisPrice()