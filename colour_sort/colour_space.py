import enum


class ColourSpace(str, enum.Enum):
    RGB = "rgb"
    LAB = "lab"
    HSV = "hsv"

    @staticmethod
    def from_str(colour_space: str) -> "ColourSpace":
        return getattr(ColourSpace, colour_space.upper())
