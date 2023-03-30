up: ## Starts ALL containers in the project
	docker-compose up -d

indenter: ## Automatically indenter djhtml
	find backend -name "*.html" | xargs djhtml -t 2 -i

autopep8: ## Automatically formats Python code to conform to the PEP 8 style guide
	find backend -name "*.py" | xargs autopep8 --max-line-length 120 --in-place

isort: ## Organizing the imports
	isort -m 3 . --skip .venv

lint: autopep8 isort indenter ## Run isort, autopep8 and indenter
