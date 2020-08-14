"""
Mon, Aug 10, 2020, 2:04 PM
https://www.pramp.com/question/Q5G1jZ1OWdtZ3GbAGpNE

Strat:
    Need to get in format of X.X.X.X

    1. look at the number of '.' I have
    2. look at the number of 'X' I have
    3. ensure 'X' is in the range (0-255) and an int
    3. return true
"""


def validateIP(ip):
    """
    @param ip: str
    @return: bool
    """
    subparts = ip.split('.')  # [X, X, X]

    if len(subparts) != 4:
        return False

    # checking all of the 'X'
    for x in subparts:
        if x.isdigit():
            x = int(x)  # caste to int
            if x < 0 or x > 255:
                return False

        else:
            return False

    # I have checked all the 'X'
    return True
