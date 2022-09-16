target: virtualenv run tests clean

VENV=mkfike_env
PYTHON=$(VENV)/bin/python

virtualenv:
	@python3 -m venv $(VENV)
	@. $(VENV)/bin/activate

run: virtualenv
	$(PYTHON) -m converter -c 30
	$(PYTHON) -m converter -f -925

tests: virtualenv
	@echo "Run Tests"
	@$(PYTHON) -m unittest

clean:
	@rm -rf __pycache__
	@rm -rf $(VENV)
	@echo "Clearing is done"