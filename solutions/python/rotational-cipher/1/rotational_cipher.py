"""
    String assessment
"""
def rotate(text, key):
    """
        This program returns the converted cipher text
        Parameters: a string text and another string key
        returns string
    """
    alpha="abcdefghijklmnopqrstuvwxyz"
    ans=""
    for char in text:
        if char.isalpha():
            val=(alpha.index(char.lower())+1+key)%26
            replaced_char=alpha[val-1]
            if char.islower():
                ans+=replaced_char
            else:
                ans+=replaced_char.upper()
        else:
            ans+=char
    return ans
        
        
