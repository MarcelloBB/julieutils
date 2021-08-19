from colorama import init, Fore, Back

class Colors:
    """
    [CLASS] COLORS:
    This class contains constants. Each constant is a color.
    They provides colors for background and foreground
    Colors with ´_´ can be interpreted as BACKGROUND. (e.g. _YELLOW means that the background color is yellow)
    The special constant ´RESET´ provides a standart output color (For foreground and background as well).
    Tip: You can use then with a ´f-string´ stuff

    """

    init()

    # Foreground stuff
    YELLOW    = Fore.YELLOW
    BLUE      = Fore.BLUE
    BLACK     = Fore.BLACK
    WHITE     = Fore.WHITE
    CYAN      = Fore.CYAN
    GREEN     = Fore.GREEN
    RED       = Fore.RED

    # Background stuff
    _YELLOW   = Back.YELLOW
    _BLUE     = Back.BLUE
    _BLACK    = Back.BLACK
    _WHITE    = Back.WHITE
    _CYAN     = Back.CYAN
    _GREEN    = Back.GREEN
    _RED      = Back.RED

    # Special Method: RESET
    RES       = (Fore.RESET + Back.RESET)