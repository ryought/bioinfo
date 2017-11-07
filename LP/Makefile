CC = gcc
CFLAGS = -Wall -lglpk  
.PHONY: all debug sanitize clean run
all: cplex  # all targets

cplex: cplex.c
	$(CC) -c $@.c; \
	$(CC) $@.o -lglpk -lm -o $@; \

run:
	./cplex

debug:
	gcc -g 
	lldb a.out

sanitize:
	gcc -g -fsanitize=address 

clean:
	rm *.o cplex

MD = pandoc -f markdown_github+footnotes+header_attributes+tex_math_dollars+compact_definition_lists+raw_tex+latex_macros -V documentclass=ltjarticle -V geometry:a4paper -V geometry:margin=3cm -V mainfont="Asana Math" -V linestretch=0.9 -V header-includes="\usepackage[version=3]{mhchem} \usepackage{url} \usepackage{wrapfig} \usepackage{graphicx}" --latex-engine=lualatex
.SUFFIXES: .md .pdf
.PHONY: all
all: report.pdf
.md.pdf: 
	$(MD) $< -o $@
