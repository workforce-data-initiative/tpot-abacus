python setup.py sdist bdist_wheel
export TWINE_USERNAME=$PYPI_USER
export TWINE_PASSWORD=$PYPI_PASSWORD
twine upload dist/*
