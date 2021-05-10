clean:
	rm -rf build
	rm -rf dist

article-clipper.pyz:
	mkdir build
	mkdir dist
	cp -r src/article-clipper/ build/
	/usr/bin/env python3 -m pip install boilerpy3 --target build/article-clipper

	/usr/bin/env python3 -m zipapp -p "/usr/bin/env python3" -o dist/article-clipper \
				 build/article-clipper

build: article-clipper.pyz

install:
	mkdir -p "${HOME}/bin"
	cp "src/scripts/gtd-clean-dir.sh" "${HOME}/bin"
	cp "src/scripts/gtd-new-forge.sh" "${HOME}/bin"
	cp "src/scripts/gtd-new-project.sh" "${HOME}/bin"
	cp "src/scripts/dev/dev_cfg.sh" "${HOME}/bin"
	cp "src/scripts/dev/dev_status.py" "${HOME}/bin"
	cp "src/scripts/youtube/youtube_parse_history.py" "${HOME}/bin"

uninstall:
	rm -f "${HOME}/bin/gtd-clean-dir.sh"
	rm -f "${HOME}/bin/gtd-new-forge.sh"
	rm -f "${HOME}/bin/gtd-new-project.sh"
	rm -f "${HOME}/bin/dev_cfg.sh"
	rm -f "${HOME}/bin/dev_status.py"
	rm -f "${HOME}/bin/youtube_parse_history.py"
