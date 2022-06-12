import codecs
import sys

import easyocr
import yaml
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from mainwindow import Ui_TranslatorMain

from utils import prtscr, ocr
from utils import translator

lang = {
    "ch_sim": "chinese"
}

class QDockWidgetDemo(QMainWindow, Ui_TranslatorMain):
    def __init__(self,
                 ocr_reader: easyocr.Reader,
                 config: dict):
        super(QDockWidgetDemo, self).__init__()
        print("[MainWindow] Loading...")

        self.reader = ocr_reader
        self.config = config
        self.translator = config['translator']
        self.appid = config['appid']
        self.api_key = config['key']

        self.dockWidget = QDockWidget('请将此窗口置于截图区域', self)
        self.dockWidget.setFloating(True)
        self.dockWidget.setWindowOpacity(0.3)

        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.dockWidget)

        self.setupUi(self)
        self.show()

        self.pbtn_translate.clicked.connect(lambda: self.translate())

    def translate(self):
        print("Making screenshot....")
        dockGeo = self.dockWidget.geometry()
        top_left = dockGeo.topLeft()
        bottom_right = dockGeo.bottomRight()
        prtscr.print_screen(top_left.x(), top_left.y(), bottom_right.x(), bottom_right.y(), "prtscr.png")
        print("Starting OCR...")
        text_lst = ocr.scan(self.reader, "prtscr.png")
        text = ''
        for t in text_lst:
            text = text + t
        result = translator.baidu.translate(self.appid, self.api_key, text).json()
        self.pte_result.setPlainText(translator.baidu.analyse_result(result))

def run(ocr_reader: easyocr.Reader,
        config: dict):
    app = QApplication(sys.argv)
    main = QDockWidgetDemo(ocr_reader, config)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
