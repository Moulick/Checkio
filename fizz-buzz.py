def checkio(number):
    
    if number % 3 ==0 and number %5 == 0:
        number = 'Fizz Buzz'
        
    elif number %3 == 0:
        number = 'Fizz'
    elif number % 5 == 0:
        number = 'Buzz'
    
    return str(number)