"""
    Binary search algorithm
"""
def find(search_list, value):
    """
        This program implements binary search algorithm iterative way
        Parameters: list of elements and search element
        returns index of element if found otherwise throws value error
    """
    start,end=0,len(search_list)-1
    while start<=end:
        mid=(start+end)//2
        if search_list[mid]==value:
            return mid
        if search_list[mid]<value:
            start=mid+1
        else:
            end=mid-1
    raise ValueError("value not in array")
