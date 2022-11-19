class ColourSortError(Exception):
    pass

class IncorrectSizeError(ColourSortError):
    def __init__(self, size):
        super().__init__(f"Image is the wrong size: {size}")
        self.size = size
