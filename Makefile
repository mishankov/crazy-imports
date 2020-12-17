install:
	( \
		. venv/bin/activate; \
		python setup.py install; \
	)

install-dev:
	( \
		python3 -m venv venv; \
		. venv/bin/activate; \
		pip install --upgrade pip; \
		pip install -r requirements-dev.txt; \
	)

lint:
	 ( \
		. venv/bin/activate; \
		python -m black .; \
	)

test: install
	( \
		. venv/bin/activate; \
		cd tests; \
		python utils/init_db.py; \
		python -m pytest; \
		rm database.sqlite3; \
	)