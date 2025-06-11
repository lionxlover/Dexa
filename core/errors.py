class DexaError(Exception):
    """Base exception for all errors in the Dexa toolchain."""
    def __init__(self, message, line=None, column=None):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(self.message)

    def __str__(self):
        if self.line and self.column:
            return f"Error at line {self.line}, col {self.column}: {self.message}"
        return f"Error: {self.message}"

class DexaLexerError(DexaError):
    """Exception raised for errors during lexical analysis."""
    pass

class DexaParserError(DexaError):
    """Exception raised for errors during parsing."""
    pass

class DexaRenderError(DexaError):
    """Exception raised for errors during rendering/exporting."""
    pass