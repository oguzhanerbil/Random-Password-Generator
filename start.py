from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from wordlist import Ui_Form
import sys
import random
from typing import Text
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QTimer
import os,sys,time,datetime


class myApp(QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.yaz)

        self.x = 10
        self.hareketettir()

    def hareketettir(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.hareketettir2)
        self.timer.start(2)

    def hareketettir2(self):
        self.x = self.x + 10
        self.ui.label.setGeometry(QtCore.QRect(self.x, 20, 81, 41))
        self.xs = str(self.x)
        time.sleep(0.05)
        if self.xs == "640":
            self.timer = QTimer()
            self.timer.timeout.connect(self.hareketettir3)
            self.timer.start(2)

    def hareketettir3(self):
        self.x = self.x - 10
        self.ui.label.setGeometry(QtCore.QRect(self.x, 20, 81, 41))
        self.xs = str(self.x)
        time.sleep(0.05)
        if self.xs == "10":
            self.hareketettir()



    def yaz(self):
        try:
            f = open(f"{self.ui.lineEdit_4.text()}WordList.txt", "x",encoding="utf-8")
        except FileExistsError:
            i = 2
            while True:
                f = open(f"{self.ui.lineEdit_4.text()}WordList_{i}.txt", "x",encoding="utf-8")
                i += 1
                break

        buyuk_harf = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
        kucuk_harf = "abcçdefgğhıijklmnoöprsştuüvyz"
        sayilar = "0123456789"
        özel_harfler = "!'^+%&/()=?_-*}][{½$#£><"

        upper = True
        lower = True
        numbers = True
        syms = True

        all = ""

        if self.ui.radioButton_7.isChecked:
            upper = True
            if upper:
                all += buyuk_harf
        
        
        if self.ui.radioButton_5.isChecked:
            lower = True
            if lower:
                all += kucuk_harf
        
        
        if self.ui.radioButton_6.isChecked:
            numbers = False  
            if numbers:      
                all += sayilar
        
        
        if self.ui.radioButton_4.isChecked:
            syms = False
            if syms:
                all += özel_harfler
        
        

        amount = int(self.ui.lineEdit_3.text())
        min = int(self.ui.spinBox_3.text())
        max = int(self.ui.spinBox_4.text())
        for x in range(amount):
            password = "".join(random.sample(all,random.randint(min,max)))
            with open(f"{self.ui.lineEdit_4.text()}WordList.txt", "a") as file:
                file.write(f"{password}\n")
        myApp()
        
        
        

def calistir():
    app = QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
calistir()