"""
    strings asssesment
"""
def is_valid(isbn):
    """
        This program valdates the given ISBN number
        Parameters: take a single strig
    """
    number=10
    total_sum=0
    valid_chars=0
    for char in isbn:
        if char.isalpha() or char.isnumeric():
            valid_chars+=1
    if valid_chars!=10:
        return False
    for char in isbn:
        if char.isnumeric():
            total_sum+=int(char)*number
            number-=1
            valid_chars+=1
        if number==1:
            if char.isalpha():
                valid_chars+=1
                if char=='X' and (total_sum+10)%11==0:
                    return True
                return False
                
    return total_sum%11==0
