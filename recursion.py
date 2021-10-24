def rFib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return rFib(n-1) + rFib(n-2)

# to access python shell in interactive mode, type in python -i recursion.py
# then to access use rFib(2) or whatever number to put in
# to quit out of interactive mode use command z