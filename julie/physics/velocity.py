
def average_speed(s1, s0, t1, t0):
    """
    [FUNC] average_speed:
    Returns the average speed.

    Where:
    
    Delta Space = (space1[s1] - space0[s0])
    Delta Time  = (time1[t1]  - time0[t0])
    """

    return ((s1-s0)/(t1-t0));


def average_acceleration(v1, v0, t1, t0):
    """
    [FUNC] average_acceleration:
    Returns the average_acceleration
    """

    return ((v1-v0)/(t1-t0));