import os
import numpy as np
import mrcfile as mf
from pathlib import Path
try:
    import estimate, args, occupy_gui              # for pyCharm
except:
    from occupy import estimate, args, occupy_gui   # for terminal use
from skimage.exposure import match_histograms

from typing import Optional
import typer


if __name__ == '__main__':
    options = typer.run(args.parse)
    estimate.occupy_run(options)


def app():
    options = typer.run(args.parse)
    estimate.occupy_run(options)

def app_gui():
    import sys
    from PyQt5 import QtCore, QtGui, QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = occupy_gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

