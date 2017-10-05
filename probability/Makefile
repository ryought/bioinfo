MD = pandoc -f markdown_github+footnotes+header_attributes+tex_math_dollars+compact_definition_lists+raw_tex  --listings -V documentclass=ltjarticle -V geometry:a4paper -V geometry:margin=3cm -V mainfont="Asana Math" -V linestretch=0.9 -V header-includes="\usepackage[version=3]{mhchem} \usepackage{url} \usepackage{wrapfig}" --latex-engine=lualatex

asai01.pdf: asai01.md
	$(MD) $< -o $@
