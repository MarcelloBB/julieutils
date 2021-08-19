def HEADER(c="=", size=50, _print=True):
    """
    [FUNC] HEADER:
    This function provides support for characters headers. Giving no arguments,
    this should print a header with ´size´ set to 50 chars, with the character
    ´=´. If you want to print the main scheme, you have to set the ´_print´ arg to True.
    Otherwise, if you just want to return the output (for using that in extern function or variable), you
    have to set to False.
    """

    if _print:
        print(f"{c}"*size)
    
    else:
        return f"{c}"*size


