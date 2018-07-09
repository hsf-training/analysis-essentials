.PHONY: all clean serve pdf

all: node_modules shell/files/data-shell.zip
	gitbook build
	@cp shell/files/data-shell.zip _book/shell/files/
	-@cp analysis-essentials.pdf _book/

serve: node_modules shell/files/data-shell.zip
	while true; do gitbook serve; sleep 5; done

pdf: node_modules
	gitbook pdf
	@mv book.pdf analysis-essentials.pdf

shell/files/data-shell.zip: $(shell find shell/data-shell/ -type f)
	cd shell && zip -r files/data-shell.zip data-shell && cd ..

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
	@ghp-import -n ./_book && git push -fq https://${GH_TOKEN}@github.com/lhcb/analysis-essentials.git gh-pages > /dev/null
