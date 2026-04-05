.PHONY: test test-verbose coverage coverage-html clean

test:
	cd scripts && python -m pytest test_gmail.py -q

test-verbose:
	cd scripts && python -m pytest test_gmail.py -v

coverage:
	cd scripts && python -m pytest test_gmail.py --cov=gmail --cov-report=term-missing -q

coverage-html:
	cd scripts && python -m pytest test_gmail.py --cov=gmail --cov-report=html -q
	@echo "Open scripts/htmlcov/index.html"

clean:
	rm -rf scripts/.coverage scripts/htmlcov scripts/__pycache__ scripts/.pytest_cache
