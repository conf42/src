jpeg:
	cd ./docs/assets && bash png_to_jpeg.sh

deps:
	pip install -r requirements.txt
	# for Ubuntu
	sudo apt-get install imagemagick || true

generate:
	python generate.py

clean:
	rm -rf ./docs/*.html

all: deps jpeg generate
