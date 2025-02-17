# AVOID Manual formatting

# Instead of doing this which seems like too much
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

# We can do this instead
for x in range(1, 11):
    """
    0 in '0:2d' is replaced with x
    The 2 is because we will use 2 *spaces*.
    - Basically because we go from 1 to 10 and 10 uses 2 spaces.
    1 in '1:3d' is replaced by x**2
    And 3 is for 3 spaces - 10^2.
    2:4d - 4 spaces - 10^3.
    ... and so on.

    All d's are because we are using integers.
    """
    print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))