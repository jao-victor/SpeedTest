from frames.classe_tela_principal import Ui_Dialog
from frames.logos import imagens
from start_speedtest import start
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from start_speedtest import start

class JanelaPrincipal(QDialog):
    
    def __init__(self):
        super().__init__()


        self.janela_principal = Ui_Dialog()
        self.janela_principal.setupUi(self)

        self.janela_principal.btn_comecar.clicked.connect(self.comecar)


    def comecar(self):

        self.janela_principal.coletando_dados.setGeometry(QtCore.QRect(150, 140, 151, 31))
        self.janela_principal.coletando_dados.setText('Buscando Resultdos...') 

        dados = start()
        self.down = str(dados[0])
        self.upld = str(dados[1])
        self.latencia = str(dados[2])
        self.latencia = self.latencia + 'ms'
        self.name_server = dados[3]

        self.janela_principal.label_valorDownload.setText(self.down)
        self.janela_principal.label_valorUpload.setText(self.upld)
        self.janela_principal.nome_servidor.setText(self.name_server)
        self.janela_principal.latencia.setText(self.latencia)

        self.janela_principal.coletando_dados.setText('Pronto...')
        self.janela_principal.coletando_dados.setGeometry(QtCore.QRect(200, 140, 151, 31))
        self.janela_principal.coletando_dados.setStyleSheet("color: #7FFF00")