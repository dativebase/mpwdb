.DEFAULT_GOAL := help

THIS_FILE := $(lastword $(MAKEFILE_LIST))

build-docs:  ## Convert the reStructuredText docs to HTML under the _build directory
	rst2html.py \
		--table-style=borderless \
		--stylesheet-path=style.css \
		docs/dativebase-morpho-parser-tutorial-1.rst \
		_build/docs/dativebase-morpho-parser-tutorial-1.html
	rst2html.py \
		--table-style=borderless \
		--stylesheet-path=style.css \
		README.rst \
		_build/README.html

help:  ## Print this help message.
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

