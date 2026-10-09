# build talk with lualatex; shared theme files and fonts live in ../theme/
export TEXINPUTS := ../theme//:
export OPENTYPEFONTS := ../theme/fonts//:

TALK := talk1
LATEX := lualatex -interaction=nonstopmode -halt-on-error

$(TALK).pdf: $(TALK).tex ../theme/icl26.sty
	$(LATEX) $(TALK) > /dev/null || (grep -A5 '^!' $(TALK).log; false)
	$(LATEX) $(TALK) > /dev/null

.PHONY: clean
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

