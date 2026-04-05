.PHONY: test test-verbose coverage coverage-html clean

SCRIPTS_DIR := scripts

test:
	cd $(SCRIPTS_DIR) && python3 -m pytest test_jira.py -q

test-verbose:
	cd $(SCRIPTS_DIR) && python3 -m pytest test_jira.py -v

coverage:
	cd $(SCRIPTS_DIR) && python3 -m coverage run --source=jira -m pytest test_jira.py -q && \
	python3 -m coverage report --show-missing

coverage-html:
	cd $(SCRIPTS_DIR) && python3 -m coverage run --source=jira -m pytest test_jira.py -q && \
	python3 -m coverage html && \
	echo "HTML report: $(SCRIPTS_DIR)/htmlcov/index.html"

clean:
	cd $(SCRIPTS_DIR) && rm -rf .coverage htmlcov __pycache__ .pytest_cache
