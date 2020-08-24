all: default

default:
	rm -rf venv
	python3 -m venv venv
	sleep 5
	# source venv/bin/activate
	#pip install -r requirements.txt

run:
	python sentiment.py

git:
	git commit -m "updates via make"
	git push

clean:
	rm -rf venv
