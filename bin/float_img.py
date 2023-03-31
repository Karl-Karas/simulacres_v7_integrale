#!/usr/bin/python3
# 
# There is NO WAY to implement floating figure in RestructuredText using LaTeX
# as redering engine (this is not the case when using rst2pdf or HTML that can
# render floating figure nearly correctly).
# To avoid hacking into docutils, I use a simple script to modify the generated
# LaTeX code.
# This script is a slightly modified version of the one proposed by user paddyg
# on Stackoverflow : 
# https://stackoverflow.com/questions/16463051/how-to-create-floating-figures-in-restructuredtext-sphinx

import sys

filename = sys.argv[1]

with open(filename, "r") as f:
  tx = f.read().splitlines()

txnew = []
flg1 = True
for line in tx:
  if line == "" and flg1:
    txnew += ["\\usepackage{wrapfig}",""]
    flg1 = False # just do this once before first blank line
  elif ("includegraphics{" in line or "includegraphics[" in line) and "hfill" in line and 'width=' in line:
    print("[DEBUG] " + sys.argv[0] + ": "  + line)
    fname = line.split("{")[2].split("}")[0]
    width = line.split("width=")[1].split("]")[0]
    width_unit = width[-2:]
    width_img = float(width[:-2])
    width_ext = width_img * 1.0 
    if '\hfill\includegraphics' in line: # i.e. right justify
      fl_type = "R"
    else:
      fl_type = "L"
    txnew += ["\\begin{wrapfigure}{" + fl_type + "}{" + str(width_ext) + width_unit + "}",
              "\\includegraphics[width = " + str(width_img) + width_unit + "]{" + fname + "}",
              "\\end{wrapfigure}"]
  else:
    txnew += [line]

txnew = "\n".join(txnew)
with open(filename, "w") as fo:
  fo.write(txnew)
