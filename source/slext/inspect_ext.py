import inspect
import os
from collections import namedtuple

Caller = namedtuple('Caller', ['frame', 'filename', 'lineno', 'function', 'code_context', 'index'])


def get_caller():
    """
    Returns:
        Caller:
    """
    frame_record = list(inspect.stack()[2])
    frame_record[1] = os.path.realpath(frame_record[1])
    return Caller(*frame_record)
