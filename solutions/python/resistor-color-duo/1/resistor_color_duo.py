"""
    List assessment
"""
def value(colors):
    """
        This program returns the color code of the given list of colors
        Parameters: single list of colors
        returns a numerical value definig the color code of resistor 
    """
    color_labels=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    ans=str(color_labels.index(colors[0]))+str(color_labels.index(colors[1]))
    return int(ans)
