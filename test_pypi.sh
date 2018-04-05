python setup.py sdist bdist_wheel
export TWINE_USERNAME=$TEST_PYPI_USER
export TWINE_PASSWORD=$TEST_PYPI_PASSWORD
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
