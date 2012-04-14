from lib2to3.fixer_base import BaseFix
from lib2to3.pygram import python_symbols as symbols

from .utils import get_leaves_after_last_newline


class FixTrailingBlankLines(BaseFix):
    u'''
    Trailing blank lines are superfluous.
    '''

    def match(self, node):
        # We only want to work with the top-level input since this should only run once.
        if node.type != symbols.file_input:
            return

        leaves_after_last_newline = get_leaves_after_last_newline(node)
        # Return any leaves with newlines.
        return [leaf for leaf in leaves_after_last_newline
                    if leaf.prefix.count('\n')]

    def transform(self, node, results):
        for index, result in enumerate(results):
            if index:
                # We've already stripped one newline. Strip any remaining
                result.prefix = result.prefix.rstrip()
                result.changed()
            else:
                # We haven't stripped any newlines yet. We need to strip all
                # whitespace, but leave a single newline.
                result.prefix = u'%s%s' % ('\n', result.prefix.rstrip())
                result.changed()