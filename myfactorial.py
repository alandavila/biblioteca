def factorial(n):
    ''' calculates factorial of input '''
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
       try:
            n = int(n)
            return n*factorial(n-1)
        except:
            print('implementation of factorial works with integers only\n');
