def get_number(prompt):
    '''Returns integer value for input. Prompt is displayed text'''
    return int(input(prompt))
    
    
def is_prime(number):
    '''Returns True for prime numbers, False otherwise'''
    #Edge Cases
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    #All other primes
    else:
        prime = True
        for check_number in range(2, int(number/2)+1):
            if number % check_number == 0:
                prime = False
                break
    return prime

def print_prime(number):
    prime = is_prime(number)
    if prime:
        descriptor = ""
    else:
        descriptor = "not "
    print(number," is ", descriptor, "prime.", sep = "", end = "\n\n")
    

    
#never ending loop

while 1 == 1:
    print_prime(get_number("Enter a number to check. Ctl-C to exit."))