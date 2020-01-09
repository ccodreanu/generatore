VERSION=0.0.1

.PHONY: all build

all: build

build:
	@python3 setup.py sdist bdist_wheel

install:
	@pip3 install dist/generatore-$(VERSION)-py3-none-any.whl

docker:
	docker build --build-arg version=$(VERSION) -t generatore:$(VERSION) .
	docker tag generatore:$(VERSION) generatore:latest

dev:
	@export PYTHONPATH=.
