project_name = monolog-python

install:
	python setup.py install

publish:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi
