python setup.py bdist_wheel

pip install -e .
pytest

python setup.py sdist
tar tzf dist/left_pad-0.0.1.tar.gz


pip install check-manifest
check-manifest --create

# deploy
python setup.py bdist_wheel sdist

pip install twine
twine upload dist/*


which gpg