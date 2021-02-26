FLAGS=


flake:
	flake8 json_schema_validator setup.py

clean:
	rm -rf `find . -name __pycache__`
	find . -type f -name '*.py[co]'  -delete
	find . -type f -name '*~'  -delete
	find . -type f -name '.*~'  -delete
	rm -rf build

run:
	python -m json_schema_validator

.PHONY: flake clean