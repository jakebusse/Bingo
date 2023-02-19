"""
This file 'patterns.py' contains basic BINGO game patterns to be checked against a players card for a win.
-----
Currently, in this file are:
 - Regular
 - Four Corners
 - Regular OR Four Corners
 - Single Postage Stamp
 - Double Postage Stamp
 - Small Round Robin
 - Full Round Robin
-----
Feel free to add to these patterns as you please. Follow the formatting guide below:
    For a single pattern that can only be completed one specific way, create a single tuple with 5 tuples inside of it.
        For instance, example_pattern = ((), (), (), (), ()) **feel free to place them on multiple lines**
    For a complex pattern that can be validated using multiple sub-patterns, create a single tuple with each
    sub-pattern tuple inside of it.
        For instance, example_complex_pattern = (((), (), (), (), ()), ((), (), (), (), ()))
    -----
    Each tuple inside of a single pattern tuple represents a vertical line on the BINGO card going from B=0 to O=4
    Example BINGO card as shown on paper then as a pattern
    B  I  N  G  O                   example_pattern = (
    1  16 31 46 61                                       (1, 2, 3, 4, 5),
    2  17 32 47 62                                       (16, 17, 18, 19, 20),
    3  18 33 48 63                                       (31, 32, 33, 34, 35),
    4  19 34 49 64                                       (46, 47, 48, 49, 50),
    5  20 35 50 65                                       (61, 62, 63, 64, 65)
                                                       )
    It should go without saying that there should only be 5 tuples inside a pattern, and 5 elements inside of a tuple.
    -----
    Mark all daubed positions with -1 and all undaubed positions with 0
    MAKE SURE TO ALWAYS DAUB THE FREE SPACE [example_pattern[2][2] = -1]
"""

regular = (
    (  # Vertical - B
        (-1, -1, -1, -1, -1),
        (0, 0, 0, 0, 0),
        (0, 0, -1, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0)
    ),
    (  # Vertical - I
        (0, 0, 0, 0, 0),
        (-1, -1, -1, -1, -1),
        (0, 0, -1, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0)
    ),
    (  # Vertical - N
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (-1, -1, -1, -1, -1),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
    ),
    (  # Vertical - G
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, -1, 0, 0),
        (-1, -1, -1, -1, -1),
        (0, 0, 0, 0, 0),
    ),
    (  # Vertical - O
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, -1, 0, 0),
        (0, 0, 0, 0, 0),
        (-1, -1, -1, -1, -1)
    ),
    (  # Horizontal - Row 1
        (-1, 0, 0, 0, 0),
        (-1, 0, 0, 0, 0),
        (-1, 0, -1, 0, 0),
        (-1, 0, 0, 0, 0),
        (-1, 0, 0, 0, 0)
    ),
    (  # Horizontal - Row 2
        (0, -1, 0, 0, 0),
        (0, -1, 0, 0, 0),
        (0, -1, -1, 0, 0),
        (0, -1, 0, 0, 0),
        (0, -1, 0, 0, 0)
    ),
    (  # Horizontal - Row 3
        (0, 0, -1, 0, 0),
        (0, 0, -1, 0, 0),
        (0, 0, -1, 0, 0),
        (0, 0, -1, 0, 0),
        (0, 0, -1, 0, 0),
    ),
    (  # Horizontal - Row 4
        (0, 0, 0, -1, 0),
        (0, 0, 0, -1, 0),
        (0, 0, -1, -1, 0),
        (0, 0, 0, -1, 0),
        (0, 0, 0, -1, 0),
    ),
    (  # Horizontal - Row 5
        (0, 0, 0, 0, -1),
        (0, 0, 0, 0, -1),
        (0, 0, -1, 0, -1),
        (0, 0, 0, 0, -1),
        (0, 0, 0, 0, -1),
    ),
    (  # Diagonal - L-R
        (-1, 0, 0, 0, 0),
        (0, -1, 0, 0, 0),
        (0, 0, -1, 0, 0),
        (0, 0, 0, -1, 0),
        (0, 0, 0, 0, -1)
    ),
    (  # Diagonal - R-L
        (0, 0, 0, 0, -1),
        (0, 0, 0, -1, 0),
        (0, 0, -1, 0, 0),
        (0, -1, 0, 0, 0),
        (-1, 0, 0, 0, 0)
    )
)

four_corners = (
    (-1, 0, 0, 0, -1),
    (0, 0, 0, 0, 0),
    (0, 0, -1, 0, 0),
    (0, 0, 0, 0, 0),
    (-1, 0, 0, 0, -1)
)

regular_four_corners = (
    regular[0],
    regular[1],
    regular[2],
    regular[3],
    regular[4],
    regular[5],
    regular[6],
    regular[7],
    regular[8],
    regular[9],
    regular[10],
    regular[11],
    four_corners
)

single_postage_stamp = (
    (  # Top Left Corner
        (-1, -1, 0, 0, 0),
        (-1, -1, 0, 0, 0),
        (0, 0, -1, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0)
    ),
    (  # Top Right Corner
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, -1, 0, 0),
        (-1, -1, 0, 0, 0),
        (-1, -1, 0, 0, 0)
    ),
    (  # Bottom Left Corner
        (0, 0, 0, -1, -1),
        (0, 0, 0, -1, -1),
        (0, 0, -1, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0)
    ),
    (  # Bottom Right Corner
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, -1, 0, 0),
        (0, 0, 0, -1, -1),
        (0, 0, 0, -1, -1)
    )
)

double_postage_stamp = (
    (  # Top
        (-1, -1, 0, 0, 0),
        (-1, -1, 0, 0, 0),
        (0, 0, -1, 0, 0),
        (-1, -1, 0, 0, 0),
        (-1, -1, 0, 0, 0)
    ),
    (  # Bottom
        (0, 0, 0, -1, -1),
        (0, 0, 0, -1, -1),
        (0, 0, -1, 0, 0),
        (0, 0, 0, -1, -1),
        (0, 0, 0, -1, -1)
    ),
    (  # Left
        (-1, -1, 0, -1, -1),
        (-1, -1, 0, -1, -1),
        (0, 0, -1, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0)
    ),
    (  # Right
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, -1, 0, 0),
        (-1, -1, 0, -1, -1),
        (-1, -1, 0, -1, -1)
    ),
    (  # Opposite - L-R
        (-1, -1, 0, 0, 0),
        (-1, -1, 0, 0, 0),
        (0, 0, -1, 0, 0),
        (0, 0, 0, -1, -1),
        (0, 0, 0, -1, -1)
    ),
    (  # Opposite - R-L
        (0, 0, 0, -1, -1),
        (0, 0, 0, -1, -1),
        (0, 0, -1, 0, 0),
        (-1, -1, 0, 0, 0),
        (-1, -1, 0, 0, 0)
    )
)

small_round_robin = (
    (0, 0, 0, 0, 0),
    (0, -1, -1, -1, 0),
    (0, -1, -1, -1, 0),
    (0, -1, -1, -1, 0),
    (0, 0, 0, 0, 0)
)

full_round_robin = (
    (-1, -1, -1, -1, -1),
    (-1, 0, 0, 0, -1),
    (-1, 0, -1, 0, -1),
    (-1, 0, 0, 0, -1),
    (-1, -1, -1, -1, -1)
)