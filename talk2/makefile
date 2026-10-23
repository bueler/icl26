# build talk with lualatex; shared theme files and fonts live in ../theme/
export TEXINPUTS := ../theme//:
export OPENTYPEFONTS := ../theme/fonts//:

TALK := talk2
LATEX := lualatex -shell-escape -interaction=nonstopmode -halt-on-error

$(TALK).pdf: $(TALK).tex ../theme/icl26.sty $(wildcard figs/*) $(wildcard tikz/*.tex) references.tex code/coprefTrue.py
	$(LATEX) $(TALK) > /dev/null || (grep -A5 '^!' $(TALK).log; false)
	$(LATEX) $(TALK) > /dev/null

# generated variant of copref.py with grid sequencing on
code/coprefTrue.py: code/copref.py
	sed 's/^gridseq = False/gridseq = True/' $< > $@

.PHONY: clean
clean:
	rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb
	rm -rf _minted*
	rm -f code/coprefTrue.py
