python setup.py sdist bdist_wheel &&
export TWINE_USERNAME=$PYPI_USER &&
export TWINE_PASSWORD=$PYPI_PASSWORD &&
python3 -m venv venv && . venv/bin/activate && pip install twine &&
twine upload dist/* &&
echo "Uploaded package to https://pypi.org/project/abacus-tpot/"
