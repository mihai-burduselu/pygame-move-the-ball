init:
	xargs sudo apt-get install -y < requirements.txt
test:
	python main.py
