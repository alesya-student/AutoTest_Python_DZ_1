from smartphone import Smartphone


catalog = [
    Smartphone("Samsung", "S23", "+79111111111"),
    Smartphone("Samsung", "A52", "+79111111112"),
    Smartphone("Samsung", "M4", "+79111111113"),
    Smartphone("Xiaomi", "Note 13", "+79111111114"),
    Smartphone("Xiaomi", "F6", "+79111111115")
]

for smartphone in catalog:
    print(f'{smartphone.make} - {smartphone.model}. {smartphone.number}')
