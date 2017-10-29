.PHONY: all clean serve

all: node_modules
	gitbook build

serve: all
	while true; do gitbook serve; sleep 5; done

node_modules:
	gitbook install

test: all
	python -m unittest tests

clean:
	@rm -rf _book
	@rm -rf node_modules
	@rm -f tests/*.pyc

publish-travis: all
	@ghp-import -n ./_book && git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git gh-pages > /dev/null
