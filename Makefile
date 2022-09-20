target: virtualenv tests clean

VENV=mkfike_env
PYTHON=$(VENV)/bin/python

#PYTHON3=$(if [ $(which python &>/dev/null | echo $?) -eq 0 ]; then PYTHON3=$python; else PYTHON3=$python3; fi)

virtualenv:
	@python3 -m venv $(VENV)
	@. $(VENV)/bin/activate
	@echo "$(VENV) was activated"

tests: virtualenv
	@echo "Run Tests"
	@python3 -m unittest

clean:
	@rm -rf __pycache__
	@rm -rf $(VENV)
	@echo "Clearing is done"