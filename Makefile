.PHONY: all build

all: build

build:
	@python3 setup.py sdist bdist_wheel