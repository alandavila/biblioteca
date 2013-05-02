def factorial(n):
    ''' calculates factorial of input '''
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)
    