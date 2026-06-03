"""
    This program assess the numbers related logic
"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot_sum=0
    for num in range(1,number):
        if number%num==0:
            aliquot_sum+=num
    if aliquot_sum==number:
        return "perfect"
    if number<aliquot_sum:
        return "abundant"
    return "deficient"
