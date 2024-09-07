from address import Address
from mailing import Mailing


to_address = Address(603000, 'Нижний Новгород', 'Ванеева', 108, 8)
from_address = Address(606000, 'Дзержинск', 'Головнина пр-т', 15, 25)
cost = 200
track = "AP-55555"

mailing = Mailing (to_address, from_address, cost, track)

print(f'Отправление {track} из {to_address} в {from_address}. Стоимость {cost} рублей.')
