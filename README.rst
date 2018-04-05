abacus-tpot
===========

Analysis Library

|License| |Python 3| |Updates| |CircleCI| |Coverage Status|
|Maintainability|

Installation
~~~~~~~~~~~~

Create a Python virtual environment then run:

.. code:: bash

    pip install abacus-tpot

Development
~~~~~~~~~~~

This project has a ``.editorconfig`` file to help contributors define
and maintain consistent coding styles between different editors and
IDEs.

We are using CircleCI for continuous integration.

Found a bug or want to propose something to the team? Create a new issue
if it is not listed `here`_. Even better, feel free to fork this repo,
make the changes and raise a PR. We’ll be more than happy to review it.

Testing
~~~~~~~

Run:

.. code:: bash

    python setup.py test

Deployment
~~~~~~~~~~

Automatic Uploading to ``testpypi`` and ``pypi`` has been set in the CI
and only develop and master branches are deployed to the package
repositories respectively.

Ready to deploy? Update the version in ``setup.py`` and create a new git
tag with ``git tag $VERSION``. Once you push the tag to GitHub with
``git push --tags`` a new CircleCI build is triggered. Once the versions
are confirmed, booyah, you have a new version uploaded.

Docs
~~~~

Going through `this jupyter notebook`_ will give you a sense of what the
abacus packs in.

.. _here: https://github.com/workforce-data-initiative/tpot-abacus/issues
.. _this jupyter notebook: https://github.com/workforce-data-initiative/tpot-abacus/blob/develop/abacus.ipynb

.. |License| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
   :target: https://opensource.org/licenses/Apache-2.0
.. |Python 3| image:: https://pyup.io/repos/github/workforce-data-initiative/tpot-abacus/python-3-shield.svg
   :target: https://pyup.io/repos/github/workforce-data-initiative/tpot-abacus/
.. |Updates| image:: https://pyup.io/repos/github/workforce-data-initiative/tpot-abacus/shield.svg
   :target: https://pyup.io/repos/github/workforce-data-initiative/tpot-abacus/
.. |CircleCI| image:: https://circleci.com/gh/workforce-data-initiative/tpot-abacus.svg?style=svg
   :target: https://circleci.com/gh/workforce-data-initiative/tpot-abacus
.. |Coverage Status| image:: https://coveralls.io/repos/github/workforce-data-initiative/abacus-tpot/badge.svg
   :target: https://coveralls.io/github/workforce-data-initiative/tpot-abacus
.. |Maintainability| image:: https://api.codeclimate.com/v1/badges/c5a146f4dd1f46bf2eaa/maintainability
   :target: https://codeclimate.com/github/workforce-data-initiative/abacus-tpot/maintainability
