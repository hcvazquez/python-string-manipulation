def print_formatted(number):
    # your code goes here
    width = len('{:b}'.format(number))
    for e in range(0, number):
        i = e+1
        print(str(i).rjust(width,' '), '{:o}'.format(i).rjust(width,' '), '{:X}'.format(i).rjust(width,' '), '{:b}'.format(i).rjust(width,' '))