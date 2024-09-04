from address import Address
class Mailing:      
       to_address = Address
       from_address = Address
       cost = 100
       track = "AP-00000"
       
       def __init__(self, to_address, from_address, cost, track):
              self.to_address = to_address
              self.from_address = from_address
              self.cost = cost
              self.track = track

       def __str__(self):
              return(f'Отправление {track} из {to_address} в {from_address}. Стоимость {cost} рублей.')

to_address = Address ("603000", "Нижний Новгород", "Ванеева", "108", "8")
from_address = Address("606000", "Дзержинск", "Головнина пр-т", "15", "25") 
cost = 200
track = "AP-55555"