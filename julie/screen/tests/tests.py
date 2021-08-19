import colors, headers, scr_config

def TESTS_():
    """
    [FUNC] TESTS_:
    Silly tests
    """
    
    # 1 - src_config
    scr_config.SET_SCREEN(); 

    # 2 - colors
    print(colors.Colors.GREEN + colors.Colors._RED + " tests __ " + colors.Colors.RES)

    # 3 - headers
    headers.HEADER()