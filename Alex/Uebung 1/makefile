TEST_CMD = python3
CHECKSTYLE_CMD = flake8

all: compile test checkstyle

compile:
	@echo "Nothing to compile for Python"

test:
	$(TEST_CMD) *test.py

checkstyle:
	$(CHECKSTYLE_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__