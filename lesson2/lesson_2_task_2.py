year = int (input('Введите год: '))

def is_year_leap(year):
    if year % 4 == 0:
        print(year, ' - год високосный')
    
    else:
        print(year, ' - год не високосный')

is_year_leap(year)