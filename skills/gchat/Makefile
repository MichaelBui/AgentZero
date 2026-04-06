.PHONY: install test test-verbose coverage coverage-html clean

install:
	pip install playwright requests pytest pytest-subtests pytest-cov pytest-mock
	python -m playwright install chromium

test:
	cd scripts && python -m pytest test_gchat.py -q

test-verbose:
	cd scripts && python -m pytest test_gchat.py -v

coverage:
	cd scripts && python -m pytest test_gchat.py --cov=gchat --cov-report=term-missing -q

coverage-html:
	cd scripts && python -m pytest test_gchat.py --cov=gchat --cov-report=html -q
	@echo "Open scripts/htmlcov/index.html"

clean:
	rm -rf scripts/.coverage scripts/htmlcov scripts/__pycache__ scripts/.pytest_cache
