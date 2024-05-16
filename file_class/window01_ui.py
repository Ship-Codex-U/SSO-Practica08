# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window01.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1059, 555)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.w_memory = QWidget(self.centralwidget)
        self.w_memory.setObjectName(u"w_memory")
        self.w_memory.setGeometry(QRect(20, 230, 1021, 271))
        self.cb_seleccionar_algoritmo = QComboBox(self.centralwidget)
        self.cb_seleccionar_algoritmo.setObjectName(u"cb_seleccionar_algoritmo")
        self.cb_seleccionar_algoritmo.setGeometry(QRect(440, 60, 231, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 60, 141, 20))
        self.b_ejecutar = QPushButton(self.centralwidget)
        self.b_ejecutar.setObjectName(u"b_ejecutar")
        self.b_ejecutar.setGeometry(QRect(440, 110, 231, 20))
        self.b_cargar_datos = QPushButton(self.centralwidget)
        self.b_cargar_datos.setObjectName(u"b_cargar_datos")
        self.b_cargar_datos.setGeometry(QRect(20, 10, 121, 24))
        self.pt_editar_texto = QPlainTextEdit(self.centralwidget)
        self.pt_editar_texto.setObjectName(u"pt_editar_texto")
        self.pt_editar_texto.setEnabled(True)
        self.pt_editar_texto.setGeometry(QRect(20, 50, 261, 131))
        self.b_reestablecer = QPushButton(self.centralwidget)
        self.b_reestablecer.setObjectName(u"b_reestablecer")
        self.b_reestablecer.setGeometry(QRect(440, 160, 231, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(740, 10, 181, 16))
        self.le_tamanioM = QLineEdit(self.centralwidget)
        self.le_tamanioM.setObjectName(u"le_tamanioM")
        self.le_tamanioM.setGeometry(QRect(860, 60, 113, 22))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(750, 60, 101, 20))
        self.cb_seleccionar_estatus = QComboBox(self.centralwidget)
        self.cb_seleccionar_estatus.setObjectName(u"cb_seleccionar_estatus")
        self.cb_seleccionar_estatus.setGeometry(QRect(860, 90, 111, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(750, 90, 101, 20))
        self.b_agregar = QPushButton(self.centralwidget)
        self.b_agregar.setObjectName(u"b_agregar")
        self.b_agregar.setGeometry(QRect(750, 160, 231, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(750, 120, 101, 20))
        self.cb_seleccionar_posicion = QComboBox(self.centralwidget)
        self.cb_seleccionar_posicion.setObjectName(u"cb_seleccionar_posicion")
        self.cb_seleccionar_posicion.setGeometry(QRect(860, 120, 111, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1059, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selecciona el algoritmo:", None))
        self.b_ejecutar.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.b_cargar_datos.setText(QCoreApplication.translate("MainWindow", u"Cargar Archivo", None))
        self.b_reestablecer.setText(QCoreApplication.translate("MainWindow", u"Reestablecer Memoria", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Configuracion de la memoria", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Estatus", None))
        self.b_agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Posicion", None))
    # retranslateUi

