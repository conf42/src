jpeg:
	cd ./docs && bash png_to_jpeg.sh

deps:
	pip install -r requirements.txt

generate:
	python generate.py

clean:
	rm -rf ./docs/*.html

all: deps jpeg generate
