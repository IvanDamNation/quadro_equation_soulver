# Program can find solutions (roots) for quadratic equations
# Can be used as module or a standalone program

# Use "calculate" for all calculation, "calc_discriminant" for
# discriminant calculation only or "get_roots" if you know
# discriminant already

# Origin code by IvanDamnNation (a.k.a. IDN)
# GNU General Public License v3.0, 2022


def calculate():
    """
    Main function. Calculate equations. Input parameters
    a, b, and c inside this function to start calculation.
    Form of the equation: a*x**2 + b*x + c = 0
    :return: None
    """
    print('Program can solve typical quadratic equation.')
    print('Equation form: a*x**2 + b*x + c = 0')

    try:
        quad_param = float(input('Input quad factor (a): '))
        unit_param = float(input(
            'Input degree of unit factor (b): '))
        wo_factor_param = float(input(
            'Input parameter without factor (c): '))

    except ValueError:
        print('Input error. Check your parameters and try again.')
        raise SystemExit(0)

    discriminant = calc_discriminant(quad_param, unit_param,
                                     wo_factor_param)

    # For no rational solution
    if discriminant < 0:
        print('There is no rational solution for this equation.')
        input('Press Enter for exit.')

    # For 1 solution
    elif discriminant == 0:
        solution_1 = get_roots(discriminant, quad_param,
                               unit_param)
        print(f'Equation have 1 solution: {solution_1: .2f}')
        input('Press Enter for exit.')

    # For 2 solutions
    else:
        solution_1, solution_2 = get_roots(discriminant, quad_param,
                                           unit_param)
        print(f'Equation have 2 solutions:{solution_1: .2f} and'
              f'{solution_2: .2f}')
        input('Press Enter for exit.')


def calc_discriminant(a: float, b: float, c: float):
    """
    Function for calculation of discriminant of equation of main
    function.
    Calc formula: D = b**2 - 4*a*c
    :param a: factor of quad parameter
    :param b: factor of degree of unit
    :param c: parameter without factor
    :return: discriminant of equation
    """

    dis = b**2 - 4*a*c
    return dis


def get_roots(dis: float, a: float, b: float):
    """
    Function gets parameters for calculation of equation's solution(s)
    Calc formula: x1 = (-b - D**0.5)/(2*a); x2 = (-b - D**0.5)/(2*a)
    :param dis: calculated discriminant
    :param a: factor of quad parameter
    :param b: factor of degree of unit
    :return: solution(s) for equation
    """

    sol1 = (-b - dis ** 0.5) / (2 * a)
    sol2 = (-b + dis ** 0.5) / (2 * a)

    if dis == 0:
        return sol1
    else:
        return sol1, sol2


# run if not a module
if __name__ == '__main__':
    calculate()
