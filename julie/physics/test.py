import energy, velocity

def TEST_():
    """
    [FUNC] TEST_:
    Silly tests
    """

    v1 = velocity.average_speed(200,0,40,0)
    v2 = velocity.average_acceleration(100,80,30,10)

    e  = energy.kinetic_energy(100,10)

    return v1, v2, e;