import codecs
import sys

import easyocr
import yaml
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
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

        # 截图悬浮窗
        self.dockWidget = QDockWidget('请将此窗口置于截图区域', self)
        self.dockWidget.setFloating(True)
        self.dockWidget.setWindowOpacity(0.3)

        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.dockWidget)

        self.setupUi(self)
        self.show()

        self.pbtn_translate.clicked.connect(lambda: self.translate())   # 截图并翻译

    def translate(self):
        if not self.translator in translator.TRANSLATOR_LST:
            print("[Window] Invalid translator")
            self.pte_result.setPlainText("无效翻译设置")
            return

        print("Making screenshot....")
        dockGeo = self.dockWidget.geometry()    # 窗口位置
        top_left = dockGeo.topLeft()    # 窗口左上角
        bottom_right = dockGeo.bottomRight()    # 窗口右下角
        prtscr.print_screen(top_left.x(), top_left.y(), bottom_right.x(), bottom_right.y(), "prtscr.png")   # 截图
        print("Starting OCR...")
        text_lst = ocr.scan(self.reader, "prtscr.png")  # 扫描截图图片
        text = ''
        for t in text_lst:
            text = text + t  # 合并扫描结果
        result = translator.translate(self.translator, self.appid, self.api_key, text).json()  # 调用翻译API
        # 翻译API错误

        self.pte_result.setPlainText(translator.analyse(self.translator, result))   # 输出结果

# 窗口启动函数
def run(ocr_reader: easyocr.Reader,
        config: dict):
    app = QApplication(sys.argv)
    main = QDockWidgetDemo(ocr_reader, config)
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
