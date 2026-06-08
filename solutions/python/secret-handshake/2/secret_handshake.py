"""
    Strings assessment
"""
def commands(binary_str):
    """
        This program provides the word for each binray bit
        Takes binary string as parameter
        Returns a list of code words
    """
    labels=['wink','double blink','close your eyes','jump']
    ans=[]
    binary_str=binary_str[::-1]
    length=len(binary_str)
    for index in range(0,length):
        if binary_str[index]=='1':
            if index>=4:
                ans=ans[::-1]
            else:
                ans.append(labels[index])
    return ans
