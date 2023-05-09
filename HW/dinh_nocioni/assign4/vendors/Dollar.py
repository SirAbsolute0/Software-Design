import random as rnd

class Vendor():
    def __call__(self):
        return (self.get_name(), self.get_price())
    
    def get_name(self):
        return "Dollar"

    def get_price(self):
        return rnd.choice([22, ValueError])
