class Product:
    def __init__(self, reference, code, description, quantity):
        self.reference = reference
        self.code = code
        self.description = description
        self.quantity = quantity

    def __repr__(self):
        return f"Product({self.reference}, Qty: {self.quantity})"