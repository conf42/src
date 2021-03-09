jpeg:
	bash png_to_jpeg.sh

deps:
	pip install -r requirements.txt

generate:
	python generate.py

clean:
	rm -rf ./docs/*.html
	rm -rf ./docs/assets/headshots/*.jpg
	rm -rf ./docs/assets/splash/*.jpg
	rm -rf ./docs/assets/podcasts/*.jpg

all: deps jpeg generate
