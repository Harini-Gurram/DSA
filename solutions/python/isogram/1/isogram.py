"""
    String assessment
"""
def is_isogram(string):
    """
        this program checks if a given string is isogram or not
        Parameters: takes input as string
        returns a boolean value
    """
    letter_set=set()
    for char in string.lower():
        if char.isalpha():
            if char not in letter_set:
                letter_set.add(char)
            else:
                return False
    return True
