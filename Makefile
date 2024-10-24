.ONESHELL:

SHELL=/bin/bash
MICROMAMBA_ACTIVATE= source ~/micromamba/etc/profile.d/mamba.sh ; micromamba activate ; micromamba activate

all: micromamba main

micromamba:
	micromamba env update --file environment.yml --prune

main:
	$(MICROMAMBA_ACTIVATE) spotify
	python3 main.py