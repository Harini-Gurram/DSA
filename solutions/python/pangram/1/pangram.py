"""
    Strings assessment
"""
english_alphabet='abcdefghijklmnopqrstuvwxyz'
def is_pangram(sentence):
    """
        This program finds if the given sentence is anagram or not
        Parameters: takes string as input
        returns a boolean value
    """
    for alphabet in english_alphabet:
        if not alphabet in sentence.lower():
            return False
    return True
    
    
