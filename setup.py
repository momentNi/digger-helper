"""Setup for pip package."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import find_packages
from setuptools import setup
from setuptools.dist import Distribution

from setuptools.command.install import install

__version__ = '1.0'
REQUIRED_PACKAGES = [
]
PROJECT_NAME = 'digger-helper'


class InstallPlatlib(install):
    def finalize_options(self):
        install.finalize_options(self)
        self.install_lib = self.install_platlib


class BinaryDistribution(Distribution):
    """This class is needed in order to create OS specific wheels."""

    def has_ext_modules(self):
        return True

    def is_pure(self):
        return False


setup(
    name=PROJECT_NAME,
    version=__version__,
    description='Open-digger helper',
    author='Shunjie Ni',
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIRED_PACKAGES,
    zip_safe=False,
    distclass=BinaryDistribution,
    cmdclass={'install': InstallPlatlib},
    # PyPI package information.
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2.0',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
    ],
    license='GPL 2.0',
    keywords='Open-digger',
)
