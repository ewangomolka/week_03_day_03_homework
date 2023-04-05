class Order():
    def __init__(self, id, name, order_date, brand, quantity):
        self.id = id
        self.name = name
        self.order_date = order_date
        self.brand = brand
        self.quantity = quantity
        self.orders = []