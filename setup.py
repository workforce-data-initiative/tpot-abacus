import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

setup(name='abacus-tpot',
      version='0.1',
      description="TPOT's analysis library funniest joke in the world",
      long_description=README,
      keywords='',
      url='https://github.com/workforce-data-initiative/abacus-tpot',
      download_url='https://github.com/workforce-data-initiative/abacus-tpot.git',
      author='Stanley Ndagi',
      author_email='stanley@brighthive.io',
      license='Apache 2.0',
      packages=['abacus_tpot'],
      zip_safe=True)
