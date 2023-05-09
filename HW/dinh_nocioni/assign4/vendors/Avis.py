class Vendor():
    def __call__(self):
        return (self.get_name(), self.get_price())
    
    def get_name(self):
        return "Avis"

    def get_price(self):
        return 20
