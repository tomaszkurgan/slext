import textwrap


def mstrip(s):
    """Strip common indents from the multiline string."""
    return textwrap.dedent(s.strip('\n'))
