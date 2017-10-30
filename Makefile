.PHONY: all clean serve pdf

all: node_modules
	gitbook build

serve: node_modules
	while true; do gitbook serve; sleep 5; done

pdf: node_modules
	gitbook pdf
	@mv book.pdf analysis-essentials.pdf

node_modules:
	gitbook install

test: all
	python -m unittest tests

clean:
	@rm -rf _book
	@rm -f book.pdf analysis-essentials.pdf
	@rm -rf node_modules
	@rm -f tests/*.pyc

publish-travis: all pdf
	@ghp-import -n ./_book && git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git gh-pages > /dev/null
