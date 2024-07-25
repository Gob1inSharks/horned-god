def diagonal_transposition(string):
    """
    Encrypts a string using diagonal transposition
    """
    return "\n".join(string[i::len(string)] for i in range(len(string)))