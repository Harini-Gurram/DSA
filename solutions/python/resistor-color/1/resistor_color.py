"""
    Lists assessment
"""
def color_code(color):
    """
        This program returns the color code of the particular color
        Parameters: takes a single string color
        returns the color code of the respective color
    """
    colors_list=colors()
    return colors_list.index(color)


def colors():
    """
        This program returns the list of the colors available
        Parameters: none
        returns the list of strings
    """
    return ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
