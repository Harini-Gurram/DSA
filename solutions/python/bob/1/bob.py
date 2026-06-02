"""
    This program is used to assess the string operations
"""
def response(hey_bob):
    """
        This function returns the variour reactions of bob
        Parameters: A string 
        returns a string
    """
    hey_bob=hey_bob.strip()
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isupper():
        return "Whoa, chill out!"
    if hey_bob.endswith("?"):
        return "Sure."
    if len(hey_bob.strip())==0:
        return "Fine. Be that way!"
    return "Whatever."
        
