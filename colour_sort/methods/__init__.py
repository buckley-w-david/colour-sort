import enum


class MethodType(str, enum.Enum):
    BRIGHTNESS = "brightness"
    AVG = "average"

    # Shift modes
    ABC = "abc"
    ACB = "acb"
    BAC = "bac"
    BCA = "bca"
    CAB = "cab"
    CBA = "cba"

    # Shift modes with clipping
    ABCC = "abcc"
    ACBC = "acbc"
    BACC = "bacc"
    BCAC = "bcac"
    CABC = "cabc"
    CBAC = "cbac"

    # Space fillinig curve approach
    ZORDER = "z-order"
    # HILBERT    = enum.auto()

    # PCA
    PCA = "pca"

    # @staticmethod
    # def from_str(sort_type: str) -> "SortType":
    #     return getattr(SortType, sort_type.upper())

    def is_clip(self):
        return False
        # return self in [
        #     SortType.ABCC,
        #     SortType.ACBC,
        #     SortType.BACC,
        #     SortType.BCAC,
        #     SortType.CABC,
        #     SortType.CBAC,
        # ]
