class Vehicle:
    def __init__(self, type: str, model: str, price: int):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str):
        if self.owner is not None:
            return "Car already sold"
        if money < self.price:
            return "Sorry, not enough money"
        self.owner = owner
        change = money - self.price
        return f"Successfully bought a {self.type}. Change: {change:.2f}"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"
        self.owner = None

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"
