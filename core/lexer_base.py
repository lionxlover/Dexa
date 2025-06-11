from collections import namedtuple
import re

Token = namedtuple('Token', ['type', 'value', 'line', 'column'])

class LexerBase:
    """A base class for simple token-based lexers."""
    def __init__(self, token_specs):
        """
        token_specs: A list of (token_type, regex_pattern) tuples.
        """
        self.token_specs = token_specs
        # Combine all regex patterns into one master pattern
        self.master_regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specs))

    def tokenize(self, code):
        """Yields a stream of tokens from the input code string."""
        line_num = 1
        line_start = 0
        for mo in self.master_regex.finditer(code):
            kind = mo.lastgroup
            value = mo.group()
            column = mo.start() - line_start + 1
            if kind == 'NEWLINE':
                line_start = mo.end()
                line_num += 1
                continue
            if kind == 'SKIP' or kind == 'COMMENT':
                continue
            yield Token(kind, value, line_num, column)