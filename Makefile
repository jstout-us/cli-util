install:
	cp "scripts/dev_cfg/dev_cfg.sh" "${HOME}/bin"
	cp "scripts/parse_youtube_history/parse_youtube_history.py" "${HOME}/bin"

uninstall:
	rm -rf "${HOME}/bin/dev_cfg.sh"
	rm -rf "${HOME}/bin/parse_youtube_history.py"
