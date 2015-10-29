_book: node_modules
	gitbook build

node_modules:
	gitbook install

clean:
	@rm -rf _book
	@rm -rf node_modules

publish-travis: _book
	@ghp-import -n ./_book && git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git gh-pages > /dev/null
