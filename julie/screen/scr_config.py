import keyboard

def SET_SCREEN():
    """
    [FUNC] SET_SCREEN:
    This function provides you to set the screen mode.
    If you want to enable the fullscreen terminal, it will be great.
    To disable fullscreen you have to execute the function once, considering you are
    fullscreen.
    """

    keyboard.press("f11")