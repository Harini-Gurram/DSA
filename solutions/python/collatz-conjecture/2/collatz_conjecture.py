"""
    This program works on numbers
"""
def steps(number):
    """
        This function returns the number of steps to deduce the number to 1
        Parameters: Accepts a single param number of type int
        returns integer
    """
    if number<1:
        raise ValueError("Only positive integers are allowed")
    steps_count=0
    if number==1:
        return 0
    while number!=1:
        if number%2==0:
            number=number//2
        else:
            number=number*3+1
        steps_count+=1
    return steps_count
