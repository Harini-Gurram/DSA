"""
    The program checks the type of triangle
"""
def equilateral(sides):
    """
        This function check whether a traingle can be formed by the given sides and if it is a                equilateral triangle
        Parameters: list of triangle sides of type int
        returns boolean value
    """
    a,b,c=sides
    if not is_triangle(sides):
        return False
    if a==b and b==c and c==a:
        return True
    return False

def isosceles(sides):
    """
        This function check whether a traingle can be formed by the given sides and if it is a                isosceles triangle
        Parameters: list of triangle sides of type int
        returns boolean value
    """
    a,b,c=sides
    if not is_triangle(sides):
        return False
    if a==b or b==c or c==a:
        return True
    return False


def scalene(sides):
    """
        This function check whether a traingle can be formed by the given sides and if it is a                scalene triangle
        Parameters: list of triangle sides of type int
        returns boolean value
    """
    a,b,c=sides
    if not is_triangle(sides):
        return False
    if a!=b and b!=c and c!=a:
        return True
    return False

def is_triangle(sides):
    """
        This function check whether a traingle can be formed by the given sides
        Parameters: list of triangle sides of type int
        returns boolean value
    """
    a,b,c=sides
    if a+b>=c and b+c>=a and c+a>=b and a>0 and b>0 and c>0:
        return True
    return False
