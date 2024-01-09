jpeg:
	bash png_to_jpeg.sh

deps:
	pip install -r requirements.txt

generate:
	python generate.py

verify:
	CHECK_REMOTE=true python generate.py

clean:
	rm -rf ./docs/*.html
	rm -rf ./docs/assets/headshots/*.jpg
	rm -rf ./docs/assets/splash/*.jpg
	rm -rf ./docs/assets/podcasts/*.jpg

env:
	python3 -m venv env

all: deps jpeg generate
