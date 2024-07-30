deployment/index.html: generate_index/*.py template.html
	./generate_index/main.py > deployment/index.html
