.PHONY: test test-verbose coverage coverage-html clean

SCRIPTS_DIR := scripts

test:
	cd $(SCRIPTS_DIR) && python3 -m pytest test_jira.py -q

test-verbose:
	cd $(SCRIPTS_DIR) && python3 -m pytest test_jira.py -v

coverage:
	cd $(SCRIPTS_DIR) && python3 -m pytest test_jira.py --cov=jira --cov-report=term-missing -q

coverage-html:
	cd $(SCRIPTS_DIR) && python3 -m pytest test_jira.py --cov=jira --cov-report=html -q && \
	echo "HTML report: $(SCRIPTS_DIR)/htmlcov/index.html"

clean:
	cd $(SCRIPTS_DIR) && rm -rf .coverage htmlcov __pycache__ .pytest_cache
