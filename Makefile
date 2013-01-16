# Makefile
RM    := rm -rfv
PWD := $(shell pwd)

.PHONY: run fox app

all: run fox

run:
	konsole --workdir "$(PWD)" -e sh -c "python app.py; echo Press any key to continue. && read -n 1"
fox:
	firefox http://localhost:5000 &
app:
	chromium-browser --app=http://127.0.0.1:5000/ &

clean:

	@- find . \( -name "*.orig" -or -name "*~" -or -name "*.pyc" -or -name "*.bak" \) -exec rm -v "{}" \;


