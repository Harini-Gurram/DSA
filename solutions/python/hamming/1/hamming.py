"""
    Strings assessment
"""
def distance(strand_a, strand_b):
    """
        This program is used to calculate the hamming distance between two strands of DNA
        Parameters: Accepts two strings a and b
        returns value error if two strings are not of equal length else returns distance of type int
    """
    if len(strand_a)!=len(strand_b):
        raise ValueError("Strands must be of equal length.")
    hamming_distance=0
    for index in range(len(strand_a)):
        if strand_a[index]!=strand_b[index]:
            hamming_distance+=1
    return hamming_distance