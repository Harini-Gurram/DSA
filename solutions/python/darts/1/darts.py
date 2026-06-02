"""
    This program is used to assess the arithmetic operations
"""
def score(x, y):
    """
        This function is used to determine the score in the darting game
        Parameters: Takes the coordinates of the target
        returns score of type int
    """
    distance=(x**2+y**2)**0.5
    if distance<=1:
        return 10
    if distance<=5:
        return 5
    if distance<=10:
        return 1
    return 0
