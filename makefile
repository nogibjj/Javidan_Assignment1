setup:
	python3 -m venv venv
	source venv/bin/activate
show:
	ls -ll
install:
	pip3 install -r requirements.txt
test:
	pytest