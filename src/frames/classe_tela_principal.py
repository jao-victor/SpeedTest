# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_prinicipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from frames.logos import imagens
import start_speedtest 

class Ui_Dialog(object):
        def setupUi(self, Dialog):
                Dialog.setObjectName("Dialog")
                Dialog.resize(472, 404)
                Dialog.setMinimumSize(QtCore.QSize(472, 404))
                Dialog.setStyleSheet("\n"
                "background-color: #05445E;")
                self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
                self.verticalLayout.setObjectName("verticalLayout")
                self.caixa_upload_download = QtWidgets.QFrame(Dialog)
                self.caixa_upload_download.setMaximumSize(QtCore.QSize(6519519, 5951519))
                self.caixa_upload_download.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.caixa_upload_download.setFrameShadow(QtWidgets.QFrame.Raised)
                self.caixa_upload_download.setObjectName("caixa_upload_download")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.caixa_upload_download)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.box_download = QtWidgets.QFrame(self.caixa_upload_download)
                self.box_download.setMaximumSize(QtCore.QSize(214, 170))
                self.box_download.setStyleSheet("")
                self.box_download.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.box_download.setFrameShadow(QtWidgets.QFrame.Raised)
                self.box_download.setObjectName("box_download")
                self.label_download = QtWidgets.QLabel(self.box_download)
                self.label_download.setGeometry(QtCore.QRect(40, 20, 91, 31))
                font = QtGui.QFont()
                font.setFamily("Tlwg Typo")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_download.setFont(font)
                self.label_download.setStyleSheet("color: #D4F1F4")
                self.label_download.setObjectName("label_download")
                self.label_valorDownload = QtWidgets.QLabel(self.box_download)
                self.label_valorDownload.setGeometry(QtCore.QRect(30, 70, 151, 51))
                font = QtGui.QFont()
                font.setFamily("Mukti Narrow")
                font.setPointSize(30)
                font.setBold(True)
                font.setWeight(75)
                self.label_valorDownload.setFont(font)
                self.label_valorDownload.setStyleSheet("color:     #FFFF00;\n"
                "")
                self.label_valorDownload.setAlignment(QtCore.Qt.AlignCenter)
                self.label_valorDownload.setObjectName("label_valorDownload")
                self.frame_3 = QtWidgets.QFrame(self.box_download)
                self.frame_3.setGeometry(QtCore.QRect(140, 15, 41, 41))
                self.frame_3.setStyleSheet("background-image: url(:/download/seta_para_baixo_redimensionada.png);\n"
                "background-position: center;\n"
                "background-repeat: no-repeat;")
                self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                self.horizontalLayout.addWidget(self.box_download)
                self.line = QtWidgets.QFrame(self.caixa_upload_download)
                self.line.setEnabled(True)
                self.line.setMinimumSize(QtCore.QSize(0, 0))
                self.line.setMaximumSize(QtCore.QSize(16777215, 150))
                self.line.setFrameShape(QtWidgets.QFrame.VLine)
                self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line.setObjectName("line")
                self.horizontalLayout.addWidget(self.line)
                self.box_upload = QtWidgets.QFrame(self.caixa_upload_download)
                self.box_upload.setMaximumSize(QtCore.QSize(214, 170))
                self.box_upload.setStyleSheet("")
                self.box_upload.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.box_upload.setFrameShadow(QtWidgets.QFrame.Raised)
                self.box_upload.setObjectName("box_upload")
                self.label_upload = QtWidgets.QLabel(self.box_upload)
                self.label_upload.setGeometry(QtCore.QRect(40, 20, 91, 31))
                font = QtGui.QFont()
                font.setFamily("Tlwg Typo")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.label_upload.setFont(font)
                self.label_upload.setStyleSheet("color:#D4F1F4;")
                self.label_upload.setAlignment(QtCore.Qt.AlignCenter)
                self.label_upload.setObjectName("label_upload")
                self.label_valorUpload = QtWidgets.QLabel(self.box_upload)
                self.label_valorUpload.setGeometry(QtCore.QRect(30, 70, 151, 51))
                font = QtGui.QFont()
                font.setFamily("Mukti Narrow")
                font.setPointSize(30)
                font.setBold(True)
                font.setWeight(75)
                self.label_valorUpload.setFont(font)
                self.label_valorUpload.setStyleSheet("color:     #FFFF00;")
                self.label_valorUpload.setAlignment(QtCore.Qt.AlignCenter)
                self.label_valorUpload.setObjectName("label_valorUpload")
                self.frame_4 = QtWidgets.QFrame(self.box_upload)
                self.frame_4.setGeometry(QtCore.QRect(130, 15, 41, 41))
                self.frame_4.setStyleSheet("background-image: url(:/upload/seta_pra_cima_redimensionada.png);\n"
                "background-position: center;\n"
                "background-repeat: no-repeat")
                self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_4.setObjectName("frame_4")
                self.horizontalLayout.addWidget(self.box_upload)
                self.verticalLayout.addWidget(self.caixa_upload_download)
                self.frame_2 = QtWidgets.QFrame(Dialog)
                self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_2.setObjectName("frame_2")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setSpacing(0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.frame_inferior = QtWidgets.QFrame(self.frame_2)
                self.frame_inferior.setMaximumSize(QtCore.QSize(454, 190))
                self.frame_inferior.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.frame_inferior.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_inferior.setObjectName("frame_inferior")
                self.btn_comecar = QtWidgets.QPushButton(self.frame_inferior)
                self.btn_comecar.setGeometry(QtCore.QRect(0, 0, 80, 41))
                font = QtGui.QFont()
                font.setFamily("Ubuntu")
                font.setBold(True)
                font.setWeight(75)
                self.btn_comecar.setFont(font)
                self.btn_comecar.setStyleSheet("QPushButton {\n"
                "border: 1px;\n"
                "background-color: #18A558;\n"
                "color: white;\n"
                "border-radius: 15px;\n"
                "}\n"
                "\n"
                "QPushButton::hover {\n"
                "    background-color:     #00FF00;\n"
                "}")
                self.btn_comecar.setObjectName("btn_comecar")
                self.btn_add = QtWidgets.QPushButton(self.frame_inferior)
                self.btn_add.setGeometry(QtCore.QRect(370, 0, 80, 41))
                self.btn_add.setStyleSheet("QPushButton {\n"
                "border: 1px;\n"
                "background-color: #18A558;;\n"
                "color: white;\n"
                "border-radius: 15px\n"
                "}\n"
                "\n"
                "QPushButton::hover {\n"
                "    background-color: #00FF00;\n"
                "}")
                self.btn_add.setObjectName("btn_add")
                self.label_servidor = QtWidgets.QLabel(self.frame_inferior)
                self.label_servidor.setGeometry(QtCore.QRect(150, 70, 57, 15))
                self.label_servidor.setStyleSheet("color: white;")
                self.label_servidor.setObjectName("label_servidor")
                self.nome_servidor = QtWidgets.QLabel(self.frame_inferior)
                self.nome_servidor.setGeometry(QtCore.QRect(210, 70, 161, 16))
                self.nome_servidor.setStyleSheet("color: white;")
                self.nome_servidor.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
                self.nome_servidor.setObjectName("nome_servidor")
                self.label_latencia = QtWidgets.QLabel(self.frame_inferior)
                self.label_latencia.setGeometry(QtCore.QRect(150, 90, 61, 16))
                self.label_latencia.setStyleSheet("color: white;")
                self.label_latencia.setObjectName("label_latencia")
                self.coletando_dados = QtWidgets.QLabel(self.frame_inferior)
                self.coletando_dados.setGeometry(QtCore.QRect(150, 140, 151, 31))
                font = QtGui.QFont()
                font.setFamily("Sawasdee")
                font.setPointSize(12)
                font.setBold(True)
                font.setItalic(True)
                font.setWeight(75)
                self.coletando_dados.setFont(font)
                self.coletando_dados.setStyleSheet("color:     #FFFF00; opacity:0;")
                self.coletando_dados.setObjectName("coletando_dados")
                self.latencia = QtWidgets.QLabel(self.frame_inferior)
                self.latencia.setGeometry(QtCore.QRect(210, 90, 57, 16))
                self.latencia.setStyleSheet("color: white;")
                self.latencia.setObjectName("latencia")
                self.logo_server = QtWidgets.QFrame(self.frame_inferior)
                self.logo_server.setGeometry(QtCore.QRect(124, 67, 25, 25))
                self.logo_server.setStyleSheet("background-image: url(:/globo/globo_redimensionado.png);\n"
                "background-repeat: no-repeat;")
                self.logo_server.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.logo_server.setFrameShadow(QtWidgets.QFrame.Raised)
                self.logo_server.setObjectName("logo_server")
                self.horizontalLayout_2.addWidget(self.frame_inferior)
                self.verticalLayout.addWidget(self.frame_2)

                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)

        def retranslateUi(self, Dialog):
                _translate = QtCore.QCoreApplication.translate
                Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
                self.label_download.setText(_translate("Dialog", "Download"))
                self.label_valorDownload.setText(_translate("Dialog", "100,00"))
                self.label_upload.setText(_translate("Dialog", "Upload"))
                self.label_valorUpload.setText(_translate("Dialog", "100,00"))
                self.btn_comecar.setText(_translate("Dialog", "Começar"))
                self.btn_add.setText(_translate("Dialog", "Add"))
                self.label_servidor.setText(_translate("Dialog", "Servidor: "))
                self.nome_servidor.setText(_translate("Dialog", "Sim Telecom"))
                self.label_latencia.setText(_translate("Dialog", "Latencia:"))
                self.coletando_dados.setText(_translate("Dialog", "Coletando dados..."))
                self.latencia.setText(_translate("Dialog", "12ms"))


        def comecar(self):
                pass

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)

        ui.btn_add.clicked.connect(Ui_Dialog.delas)

        Dialog.show()
        sys.exit(app.exec_())

