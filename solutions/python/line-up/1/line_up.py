"""
    String formatting exercise
"""
def line_up(name, number):
    """
        This program returns the formatted string with given name and number
        Takes two parameters of type int number and type string name
        Returns string
    """
    return f"{name}, you are the {get_number_string(number)} customer we serve today. Thank you!"
def get_number_string(number):
    """
        This program is used to return the suffix for a certain number
        Takes number of type int as parameter
        Returns string
    """
    num=str(number)
    if num[-1]=='1' and num[-2:]!='11':
        return num+"st"
    if num[-1]=='2' and num[-2:]!='12':
        return num+"nd"
    if num[-1]=='3' and num[-2:]!='13':
        return num+"rd"
    return num+"th"
