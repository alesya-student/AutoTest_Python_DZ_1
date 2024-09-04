n = int(input())
def fizz_buzz(n):
    for n in range(1, n+1): # в этом случае отработают все числа из промежутка от 1 до заданного
        if (n % 3 == 0) and (n % 5 == 0):
            print('FizzBuzz')
    
        elif (n % 3 == 0):
            print('Buzz')

        elif (n % 5 == 0):
            print('Fizz')

        else:
            print(n)

fizz_buzz(n)