import os
from setuptools import setup, find_packages

package_name = 'slext'
source_dir = 'source'

packages = find_packages(os.path.join('.', source_dir))
package_dir = {
    '': source_dir,
}

install_requires = []
dependency_links = []

READTHEDOCS_PROJECT = os.environ.get('READTHEDOCS_PROJECT')
if READTHEDOCS_PROJECT:
    if READTHEDOCS_PROJECT == package_name:
        install_requires.append('sphinx_theme<=999')
        dependency_links.append('https://github.com/tomaszkurgan/sphinx_theme/archive/master.zip#egg=sphinx_theme-999')

setup(
    name=package_name,
    version='0.0.1',
    packages=packages,
    package_dir=package_dir,
    install_requires=install_requires,
    dependency_links=dependency_links,
)
