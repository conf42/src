jpeg:
	bash png_to_jpeg.sh

deps:
	pip install -r build/requirements.txt

generate:
	python -m build.generate

transcribe:
	python -m build.transcribe

verify:
	CHECK_REMOTE=true python -m build.generate

clean:
	rm -rf ./docs/*.html
	rm -rf ./docs/assets/headshots/*.jpg
	rm -rf ./docs/assets/splash/*.jpg
	rm -rf ./docs/assets/podcasts/*.jpg

env:
	python3 -m venv env

all: deps jpeg generate transcribe verify
