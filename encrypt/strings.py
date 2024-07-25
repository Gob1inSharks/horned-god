def remove_spaces(string):
    """
    Removes spaces from a string
    """
    return string.replace(" ", "")

def decaptilize(string):
    """
    Decaptilizes a string
    """
    return string.lower()

def capitalize(string):
    """
    Capitalizes a string
    """
    return string.capitalize()

def remove_punctuation(string):
    """
    Removes punctuation from a string
    """
    return string.translate(str.maketrans("", "", string.punctuation))

