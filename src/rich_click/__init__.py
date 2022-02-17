"""
rich-click is a minimal Python module to combine the efforts
of the excellent packages 'rich' and 'click'.

The intention is to provide attractive help output from
click, formatted with rich, with minimal customisation required.
"""

__version__ = "0.4.0.dev0"

from click import *
from .rich_click import RichGroup
from .rich_click import RichCommand


def group(*args, cls=RichGroup, **kwargs):
    from click import group as click_group

    return click_group(*args, cls=cls, **kwargs)


def command(*args, cls=RichCommand, **kwargs):
    from click import command as click_command

    return click_command(*args, cls=cls, **kwargs)
