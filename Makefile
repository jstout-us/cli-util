install:
	mkdir -p "${HOME}/bin"
	cp "src/scripts/dev/dev_cfg.sh" "${HOME}/bin"
	cp "src/scripts/dev/dev_project_dir.sh" "${HOME}/bin"
	cp "src/scripts/dev/dev_status.py" "${HOME}/bin"
	cp "src/scripts/youtube/youtube_parse_history.py" "${HOME}/bin"

uninstall:
	rm -f "${HOME}/bin/dev_cfg.sh"
	rm -f "${HOME}/bin/dev_project_dir.sh"
	rm -f "${HOME}/bin/dev_status.py"
	rm -f "${HOME}/bin/youtube_parse_history.py"
