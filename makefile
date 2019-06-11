venv_set:.venv
	./.venv/bin/activate
venv_unset:.venv
	deactivate
upload: venv_set venv_unset
	venv_set
	rm -rf dist/*
	python setup.py sdist
	python setup.py publish
	twine upload dist/*
	rm -rf dist/*
	venv_unset

upload_test: venv_set venv_unset
	venv_set
	rm -rf dist/*
	python setup.py sdist
	python setup.py publish
	twine upload --repository pypitest dist/*
	rm -rf dist/*
	venv_unset
