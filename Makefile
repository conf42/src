jpeg:
	bash png_to_jpeg.sh

deps:
	pip install -r requirements.txt

generate:
	python generate.py

clean:
	rm -rf ./docs/*.html
	rm -rf ./docs/assets/headshots/*.jpeg
	rm -rf ./docs/assets/splash/*.jpeg
	rm -rf ./docs/assets/podcasts/*.jpeg

all: deps jpeg generate
