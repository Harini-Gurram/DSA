"""
    Strings assessment
"""
def commands(binary_str):
    """
        This program provides the word for each binray bit
        Takes binary string as parameter
        Returns a list of code words
    """
    labels=["wink","double blink","close your eyes","jump"]
    ans=[]
    binary_str=binary_str[::-1]
    l=len(binary_str)
    for i in range(0,l):
        if binary_str[i]=='1':
            if i>=4:
                ans=ans[::-1]
            else:
                ans.append(labels[i])
    return ans
