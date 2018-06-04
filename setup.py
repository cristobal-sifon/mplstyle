from __future__ import print_function

import os

path = os.path.join(os.getcwd(), 'mplstyle')

msg = """
Custom matplotlib styles library.

In order to activate the libraries in this repository, please execute
the following commands

$ cd ~/.matplotlib
$ ln -s {0} stylelib

you may then activate any of the available styles with

> plt.style.use(style)
""".format(path)

print(msg)
