"""
    Lists assessment
"""
def flatten(iterable):
    """
        This programs recursively flattens the list of lists
        Parameters: Takes single nested list object
        Returns flatten list
    """
    flat_list=[]
    for item in iterable:
        if isinstance(item,list):
            temp_list=flatten(item)
            if len(temp_list)>0:
                flat_list.extend(temp_list)
        elif item is not None:
            flat_list.append(item)
    return flat_list
