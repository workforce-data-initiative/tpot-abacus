python setup.py sdist bdist_wheel &&
export TWINE_USERNAME=$TEST_PYPI_USER &&
export TWINE_PASSWORD=$TEST_PYPI_PASSWORD &&
python3 -m venv venv && . venv/bin/activate && pip install twine &&
twine upload --repository-url https://test.pypi.org/legacy/ dist/* &&
echo "Uploaded package to https://test.pypi.org/project/abacus-tpot/"
