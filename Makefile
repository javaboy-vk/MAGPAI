.PHONY: test docs clean

test:
	pytest

docs:
	mkdocs serve

clean:
	python scripts/clean_generated.py
