"""
    This program is defined for the determination of a leap year
"""
def leap_year(year):
    """
        The function leap_year determines whether a given year is leap year or not
        Parameters: year of type int
        returns boolena value
    """
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            return False
        return True
    return False
