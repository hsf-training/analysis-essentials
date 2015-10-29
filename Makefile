_book: node_modules
	gitbook build

node_modules:
	gitbook install

test: _book
	python -m unittest tests

clean:
	@rm -rf _book
	@rm -rf node_modules
	@rm -f tests/*.pyc

publish-travis: _book
	@ghp-import -n ./_book && git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git gh-pages > /dev/null
