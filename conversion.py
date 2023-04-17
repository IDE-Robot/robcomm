import ast

# This file includes helper functions to convert values to and from strings
# and to and from the robot's internal representation of values.


def to_string(value):
    """
    Converts a value to a string that can be sent to the robot

        e.g. [1, 2, 3] -> "[1, 2, 3]", 1.0 -> "1.0", True -> "True"

    """
    return value.__str__()


def from_string(value):
    """
    Converts a string received from the robot to a specific type,

        e.g. "[1, 2, 3]" -> [1, 2, 3], "1.0" -> 1.0, "TRUE" -> True

    If the type cannot be determined, the value is returned as a string

    You can use type hints to specify the type of the returned value:

        coords: List[float] = from_string(value)
    """
    return ast.literal_eval(value.replace("TRUE", "True").replace("FALSE", "False"))
