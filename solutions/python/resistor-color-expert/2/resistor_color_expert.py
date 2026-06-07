"""
    List and string assessment
"""
def resistor_label(colors):
    """
        This program returns the resistance value along with tolerance
        Parameters: takes list of colors
        returns resistance value as string
    """
    color_labels = ["black", "brown", "red", "orange", "yellow", 
                    "green", "blue", "violet", "grey", "white"]

    tolerance_bands={"grey":"0.05%","violet":"0.1%","blue":"0.25%","green":"0.5%","brown":"1%","red":"2%","gold":"5%","silver":"10%"}

    if len(colors)==1 and colors[0]=="black":
        return "0 ohms"
    val1 = color_labels.index(colors[0])
    val2 = color_labels.index(colors[1])
    multiplier=color_labels.index(colors[-2])
    tolerance=tolerance_bands[colors[-1]]

    base_value=0
    if len(colors)>4:
        val3=color_labels.index(colors[2])
        base_value=val1*100+val2*10+val3
    else:
        base_value=val1*10+val2
    total_ohms = base_value * (10 ** multiplier)
    
    if total_ohms >= 1_000_000_000:
        return f"{total_ohms /1_000_000_000:g} gigaohms ±{tolerance}"
    if total_ohms >= 1_000_000:
        return f"{total_ohms / 1_000_000:g} megaohms ±{tolerance}"
    if total_ohms >= 1_000:
        return f"{total_ohms / 1_000:g} kiloohms ±{tolerance}"
    return f"{total_ohms} ohms ±{tolerance}"
