clean:
	rm -rf build
	rm -rf dist
	pyclean -v .

clip-article:
	mkdir build
	mkdir dist
	pyinstaller src/clip-article/cli.py \
				--add-data "/usr/local/lib/python3.8/dist-packages/goose3:goose3" \
				--add-data "/usr/local/lib/python3.8/dist-packages/newspaper:newspaper" \
				--distpath dist/ \
				--workpath build/clip-article \
				--paths /usr/local/lib/python3.6/dist-packages \
				--name clip-article \
				--onefile

build: clip-article

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
