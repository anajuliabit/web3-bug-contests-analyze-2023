(TeX-add-style-hook
 "caption2"
 (lambda ()
   (TeX-add-symbols
    '("subcapstyle" 1)
    '("onelinecaption" 1)
    '("usecaptionstyle" 1)
    '("captionstyle" 1)
    '("dummycaptionstyle" 2)
    '("renewcaptionstyle" 1)
    '("newcaptionstyle" 1)
    '("defcaptionstyle" 1)
    "captionfont"
    "captionmargin"
    "captionwidth"
    "captionindent"
    "setcaptionmargin"
    "setcaptionwidth"
    "normalcaptionparams"
    "caption"
    "captionlinewidth"
    "usecaptionmargin"
    "subfigcapwidth"
    "setsubcapmargin"
    "setsubcapwidth"
    "subcaplabelsep"
    "subcapindent"
    "subcaplabeldelim"
    "captionsize"
    "captionof"
    "captionlabelfont"
    "captionlabeldelim"
    "captionlabelsep"
    "captionlabel"
    "captiontext"
    "setsubcapstyle"
    "subcapfont")
   (LaTeX-add-lengths
    "abovecaptionskip"
    "belowcaptionskip"))
 :latex)

