def pythagoras(a, b, c):
    """
    This function take 3 arguments as input of sides of triangle and check whether
    the 3 inputs satisfy following equation or not:
    a**2 + b**2 = c**2
    where  a and b are first two inputs as well as 2 sides of a right-angled triangle
    whereas c is third input and represents the hypotenuse of a right-angled triangle
    :return: "Yes", if above equation satisfy or else returns "No"
    """
    return "Yes" if (a**2 +b**2) == c**2 else "No"
