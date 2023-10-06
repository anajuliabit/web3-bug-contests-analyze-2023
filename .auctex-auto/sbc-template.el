(TeX-add-style-hook
 "sbc-template"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "a4paper" "top=3.5cm" "left=3cm" "right=3cm" "bottom=2.5cm") ("caption2" "bf" "sf" "footnotesize" "indent")))
   (TeX-run-style-hooks
    "geometry"
    "caption2"
    "times"
    "titlesec")
   (TeX-add-symbols
    '("authortag" 1)
    '("email" 1)
    '("inst" 1)
    "XIIIPT"
    "XVIPT"
    "instnum"
    "nextinstitute"
    "protect"
    "address"
    "maketitleOLD")
   (LaTeX-add-environments
    '("thebibliography" 1)
    "resumo")
   (LaTeX-add-counters
    "instn"))
 :latex)

