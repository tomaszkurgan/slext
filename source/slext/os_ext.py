import errno
import shutil
import sys

import os


def copy_tree(src, dst, override=False, ignore_errors=False, on_error=None):
    if ignore_errors:
        def on_error(*args):
            pass
    elif on_error is None:
        def on_error(*args):
            exec 'raise'

    dst_exists = False
    try:
        os.makedirs(dst)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        dst_exists = True

    for item in os.listdir(src):
        item_path = os.path.join(src, item)
        item_dst_path = os.path.join(dst, item)

        if os.path.isdir(item_path):
            copy_tree(item_path, item_dst_path, override, ignore_errors, on_error)
        else:
            try:
                shutil.copy2(item_path, item_dst_path)
            except Exception:
                on_error(item_path, item_dst_path, sys.exc_info())

    if not dst_exists:
        try:
            shutil.copystat(src, dst)
        except OSError as e:
            if WindowsError is not None and isinstance(e, WindowsError):
                # Copying file access times may fail on Windows
                pass
            else:
                on_error(src, dst, sys.exc_info())


