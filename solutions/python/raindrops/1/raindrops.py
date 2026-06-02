"""
    This program is written to assess the conditionals in python
"""
def convert(number):
    """
        This function is used to find the sound of the number
        Parameters: number of type integer
        returns a string value
    """
    result=""
    flag=False
    if number%3==0:
        result+="Pling"
        flag=True
    if number%5==0:
        result+="Plang"
        flag=True
    if number%7==0:
        result+="Plong"
        flag=True
    if flag:
        return result
    return str(number)
    