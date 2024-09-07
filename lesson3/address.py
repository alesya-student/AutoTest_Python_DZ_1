class Address:
   
    def __init__(self, index, city, street, house, apart):
        self.index = index
        self.city = city
        self.street = street 
        self.house = house
        self.apart = apart

    def __str__(self):
        return f'{self.index}, {self.city}, {self.street}, {self.house} - {self.apart}'
