"""
    Strings assessment
"""
def is_pangram(sentence):
    """
        This program finds if the given sentence is anagram or not
        Parameters: takes string as input
        returns a boolean value
    """
    english_alphabet='abcdefghijklmnopqrstuvwxyz'
    return all(alphabet in sentence.lower() for alphabet in english_alphabet)
    
    
