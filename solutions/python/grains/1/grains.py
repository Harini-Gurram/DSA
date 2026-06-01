"""
    This program is used to calculate the total number of grains on borad or grains count on each square
"""
def square(number):
    """
        This function is used to calcuate the total number of grains on the given square
        Parameters: single square number
        returns int 
    """
    if number<1 or number>64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total():
    """
        This function is used to calcuate the total number of grains on the board
        returns int 
    """
    return 2**(64)-1
