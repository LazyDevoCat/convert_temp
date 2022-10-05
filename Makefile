target: virtualenv tests

VENV=mkfike_env
PYTHON=$(VENV)/bin/python

#PYTHON3=$(if [ $(which python &>/dev/null | echo $?) -eq 0 ]; then PYTHON3=$python; else PYTHON3=$python3; fi)
# https://habr.com/ru/post/211751/

.PHONY: help
help:           ## Show this help.
	@printf "$(GREEN)	help		$(NC)	Display this help message\n"
	@printf "$(GREEN)	virtualenv	$(NC)	Activate virtual environment\n"
	@printf "$(GREEN)	tests		$(NC)	Run unittests\n"
	@printf "$(GREEN)	clean		$(NC)	Delete virtual environment\n"


virtualenv:
	@python3 -m venv $(VENV)
	@. $(VENV)/bin/activate
	@echo "$(VENV) was activated"

tests: virtualenv
	@echo "Run Tests"
	@python3 -m unittest


.PHONY: clean
clean:
	@rm -rf __pycache__
	@rm -rf $(VENV)
	@echo "Clearing is done"