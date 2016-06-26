echo Old, do not use
exit 1
gs \
 -o test3-content.pdf \
 -sDEVICE=pdfwrite \
 -dDEVICEWIDTHPOINTS=585 -dDEVICEHEIGHTPOINTS=738 \
 -dFIXEDMEDIA \
 -dPDFSETTINGS=/prepress \
 -dPDFFitPage -r300 \
 -dCompatibilityLevel=1.4 \
  JL0x7-content.pdf
