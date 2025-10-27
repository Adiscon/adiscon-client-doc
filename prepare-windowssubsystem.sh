#!/bin/sh

echo :WindowsBatch:E::bat::/init: > /proc/sys/fs/binfmt_misc/register

# Install sphinx, sphinxcontrib-htmlhelp, pdflatex, rst2pdf
pip install sphinx sphinxcontrib-htmlhelp pdflatex rst2pdf 
