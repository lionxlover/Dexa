from abc import ABC

class ASTNode(ABC):
    """Base class for all Abstract Syntax Tree nodes."""
    def __repr__(self):
        # Dynamically create a representation string from the node's attributes.
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        attr_str = ', '.join(f"{k}={repr(v)}" for k, v in attrs.items())
        return f"{self.__class__.__name__}({attr_str})"

class Literal(ASTNode):
    """Represents a literal value like a number, string, or boolean."""
    def __init__(self, value, value_type):
        self.value = value
        self.type = value_type

class Identifier(ASTNode):
    """Represents a named identifier, like a variable or a function name."""
    def __init__(self, name):
        self.name = name

class BinaryOp(ASTNode):
    """Represents a binary operation (e.g., a + b)."""
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right