.PHONY: all build

all: build

build:
	@python3 setup.py sdist bdist_wheel

install:
	@pip3 install dist/generatore-*.whl

dev:
	@export PYTHONPATH=.