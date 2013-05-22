
Requirements
============

* ctex
* amsmath, amsfonts
* hyperref
* fontspec
* tikz
* float
* tikz-qtree
* geometry
* graphicx
* subcaption


Useful AucTex Shortcut
======================

* `C-c C-c` compile
* `C-c C-e` insert env
* `C-c C-s` insert section
* `C-c C-f C-e` insert `emph`
* `C-c C-f C-t` insert `texttt`
* `C-c ;` comment or uncomment region
* `C-c RET` or `C-c C-m` insert macro (input etc)
* `C-c ^` return to main tex file


Note
====

When building pdf document, don't forget to run the scripts
under `scripts`, in case plot data be modified. The command
should be `/path/to/ipython --pylab=auto script.py`.

Dependency `minted` has been removed.

Add `-shell-escape` so that `minted` can work normally.


