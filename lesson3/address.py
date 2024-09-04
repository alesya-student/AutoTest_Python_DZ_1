class Address:
    index = "000000"
    city = "Москва"
    street = "Ленина"
    house = "10"
    apart = "100"
    
    def __init__(self, index, city, street, house, apart):
        self.index = index
        self.city = city
        self.street = street 
        self.house = house
        self.apart = apart

    def __str__(self):
        return(f'{self.index}, {self.city}, {self.street}, {self.house} - {self.apart}')

