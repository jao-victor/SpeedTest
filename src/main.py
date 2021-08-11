# id no servidor da netware 39487
# Coxim TJNET 11038
# ideal gigarede anastácio 37365


from frames.tela_principal import JanelaPrincipal
import sys
from PyQt5 import QtWidgets


app = QtWidgets.QApplication([])

tela = JanelaPrincipal()
tela.exec()

sys.exit(app.exec_())
