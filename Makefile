BIN_NAME=nocodb-to-gpt-via-api
BIN_VERSION=0.0.3
BIN_DATE=$(shell date +%FT%T%z)

test:
	pytest

