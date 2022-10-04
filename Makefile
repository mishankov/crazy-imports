# ----------- Dev tools

dev-env:
	( \
		rm -rf venv; \
		python3 -m venv venv; \
		. venv/bin/activate; \
		pip install --upgrade pip; \
		pip install -r requirements-test.txt -r requirements-dev.txt; \
	)

dev-lint:
	( \
		. venv/bin/activate; \
		python -m black .; \
	)

dev-install: dev-lint
	( \
		. venv/bin/activate; \
		pip uninstall crazyimports -y; \
		python setup.py install; \
	)

dev-test: dev-install
	( \
		. venv/bin/activate; \
		mkdir tests/test_data/generated/; \
		python tests/utils/init_data.py; \
		coverage run -m pytest; \
		rm -rf tests/test_data/generated/; \
		coverage html; \
		coverage report; \
	)

dev-prepare-docs:
	( \
		cp README.md docs/index.md; \
		cp CONTRIBUTING.md docs/contributing.md; \
	)

dev-prepare-push: dev-lint dev-prepare-docs


# ----------- CI tools

ci-lint:
	pip install black
	black --check .

ci-test:
	pip install -r requirements-test.txt
	mkdir tests/test_data/generated/
	python tests/utils/init_data.py
	coverage run -m pytest
	coverage xml

ci-publish:
	python -m pip install --upgrade pip
	pip install setuptools wheel twine
	python setup.py sdist bdist_wheel
	twine upload dist/*

ci-publish-docs:
	pip install mkdocs-material
	cp README.md docs/index.md
	cp CONTRIBUTING.md docs/contributing.md
	mkdocs gh-deploy --force
