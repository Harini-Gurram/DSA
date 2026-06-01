"""
    This program is defined to determine whether the number is armstrong or not
"""
def is_armstrong_number(number):
    """
        This function determines whether the given number is armstrong number or not
        Parameters: number of type int
        returns boolean value
    """
    power=len(str(number))
    total_value=0
    duplicate_number=number
    while number>0:
        rem=number%10
        number=number//10
        total_value+=rem**power
    return total_value==duplicate_number