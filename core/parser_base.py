from .errors import DexaParserError

class ParserBase:
    """
    A base class for simple recursive descent parsers.
    """
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.pos = 0

    def parse(self):
        """Main entry point for parsing."""
        raise NotImplementedError("Each parser must implement a `parse` method.")

    def current_token(self):
        """Returns the current token without consuming it."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def advance(self):
        """Consumes the current token and moves to the next one."""
        token = self.current_token()
        self.pos += 1
        return token

    def consume(self, expected_type):
        """Consumes the next token if it matches the expected type, otherwise raises an error."""
        token = self.current_token()
        if token is None:
            raise DexaParserError(f"Unexpected end of input. Expected {expected_type}.")
        if token.type == expected_type:
            return self.advance()
        raise DexaParserError(
            f"Expected token of type {expected_type} but got {token.type}",
            line=token.line,
            column=token.column
        )