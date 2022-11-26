import string, sys
start = print("\033[44m Welcome to the basic polynomial calculator code. \033[0m")
def polynomial(x, coef):
    sum = 0
    while 1:
        sum = sum + coef[0]
        coef = coef[1:]
        if not coef:
            break
        sum = sum * x

    return sum



def calculate(prompt):
    line = input(prompt)
    if line == 'quit': sys.exit(0)

    turnaround = [];
    for s in str.split(line):
        try:
            turnaround.append(int(s))
        except ValueError:
            print('Conversion of', s, 'failed.')
            return []

    return turnaround



def polynomial_str(p):
    exponential_function = len(p)
    turnaround = ''
    while p:
        exponential_function = exponential_function - 1
        coef = p[0]
        p = p[1:]
        if coef == 0:
            continue

        if turnaround:
            if coef >= 0:
                turnaround = turnaround + ' + '
            else:
                coef = -coef
                turnaround = turnaround + ' - '


        if coef != 1 or exponential_function == 0:
            turnaround = turnaround + str(coef)
            if exponential_function != 0: turnaround = turnaround + '*'

        if exponential_function != 0:
            turnaround = turnaround + 'x'
            if exponential_function != 1: turnaround = turnaround + '^' + str(exponential_function)


    if not turnaround: turnaround = '0'

    return turnaround


try:
    while 1:
        while 1:
            poly = calculate("""\033[34m Enter a polynomial coefficients with spaces
\033[32m (For ex: if you press 2 3 7, your polynomial is 2*x^2 + 3*x + 7) : \033[0m 
            """)
            if poly:
                break
            print('Try again.')

        while 1:
            resp = input('\033[34m Enter x value: ')
            if resp == 'quit': sys.exit(0)
            if not resp: break
            try:
                x = int(resp)
            except ValueError:
                print("That doesn't look like an integer.  Please try again.")
            else:
                print('\033[95m p(x) =', polynomial_str(poly))
                print('\033[95m p(' + str(x) + ') =', polynomial(x, poly))

except (EOFError, KeyboardInterrupt):
    print()
