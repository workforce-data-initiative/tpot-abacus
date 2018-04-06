import os
import sys
from setuptools import setup

from setuptools.command.install import install


VERSION = "0.92"
TAG = os.getenv('CIRCLE_TAG')


def read(fname):
    """print long description"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        if TAG != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                TAG, VERSION
            )
            sys.exit(info)


setup(
    name='abacus-tpot',
    packages=['abacus_tpot'],
    version=VERSION,
    description="TPOT's analysis library",
    long_description=read('README.rst'),
    keywords=['analysis', 'data', 'tpot', 'library'],
    url='https://github.com/workforce-data-initiative/abacus-tpot',
    download_url='https://github.com/workforce-data-initiative/abacus-tpot/archive/{}.tar.gz'.format(TAG),
    author='Stanley Ndagi, Tom Plagge',
    author_email='stanley@brighthive.io, tom@brighthive.io',
    license='Apache 2.0',
    zip_safe=True,
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)
