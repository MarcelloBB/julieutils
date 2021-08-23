import equations

def TESTS_():
    """
    [FUNC] TESTS_:
    Silly tests
    """

    # IN
    RUN = True

    while RUN:
        a  = float(input("\nA : "));
        b  = float(input("\nB : "));
        c  = float(input("\nC : "));

        # CREATE
        eq = equations.Equation(a, b, c);

        print()

        # SOLVE
        print(f"RESULT >>> {eq.solve()}")

        print()
        
        if input("CONTINUE ? (y/n) ") != "y": RUN = False; break;