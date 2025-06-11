from enum import Enum, auto

class DexaType(Enum):
    """Enumeration of core Dexa data types."""
    INT = auto()
    FLOAT = auto()
    STRING = auto()
    BOOL = auto()
    ARRAY = auto()
    STRUCT = auto()
    ENUM = auto()
    ANY = auto()
    VOID = auto()

def infer_type(value):
    """Infers the DexaType from a Python value."""
    if isinstance(value, bool):
        return DexaType.BOOL
    if isinstance(value, int):
        return DexaType.INT
    if isinstance(value, float):
        return DexaType.FLOAT
    if isinstance(value, str):
        return DexaType.STRING
    if isinstance(value, list):
        return DexaType.ARRAY
    return DexaType.ANY