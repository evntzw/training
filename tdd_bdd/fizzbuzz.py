def fizzbuzz(n: int):
    if modulo(n,3) and modulo (n, 5):
        return 'FizzBuzz'
    elif modulo(n, 3):
        return 'Fizz'
    elif modulo(n, 5):
        return 'Buzz'
    
def modulo(n: int, m: int):
    return n % m == 0