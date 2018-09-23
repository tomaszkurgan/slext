import os

from slext import os_ext


class Test_copy_tree(object):
    def test_copy_with_src_root_dir(self, resource_dir, temp_dir):
        src_dir = os.path.join(resource_dir, 'src', 'payload')
        dst_dir = os.path.join(temp_dir, 'dst', 'payload')

        os_ex.copy_tree(src_dir, dst_dir)

        assert os.path.exists(os.path.join(temp_dir, 'dst', 'payload', 'a.txt'))
