"""
    Lists and string assessment
"""
def label(colors):
    """
        This program takes list of colors and returns the reistance value in terms of ohms
        Parameter: takes a single list of color codes
        returns a string defining the resistance value in terms of ohms
    """
    color_labels=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    
    val1 = color_labels.index(colors[0])
    val2 = color_labels.index(colors[1])
    multiplier = color_labels.index(colors[2])

    base_value = (val1 * 10) + val2
    total_ohms = base_value * (10 ** multiplier)

    if total_ohms >= 1_000_000_000:
        return f"{total_ohms // 1_000_000_000} gigaohms"
    if total_ohms >= 1_000_000:
        return f"{total_ohms // 1_000_000} megaohms"
    if total_ohms >= 1_000:
        return f"{total_ohms // 1_000} kiloohms"
    return f"{total_ohms} ohms"
        
