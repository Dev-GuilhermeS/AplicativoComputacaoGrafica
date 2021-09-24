import sys
import subprocess
from tkinter import messagebox
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QGridLayout, QWidget, QMessageBox, QSlider
from PyQt5.QtCore import QSize, Qt

class MyWindow(QMainWindow) :
    def __init__(self) :
        super(MyWindow, self).__init__()
        self.setup_main_window()
        self.initUI()

    def setup_main_window(self) :
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Hello World - P . D . I")
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.layout = QGridLayout()
        self.wid.setLayout(self.layout)

    def initUI(self) :
        #Barra Menu
        self.barrademenu = self.menuBar()

        #Menus
        self.menuarquivo = self.barrademenu.addMenu("&Arquivo")
        self.menuTransformar = self.barrademenu.addMenu("&Transformações")
        self.menuajustes = self.barrademenu.addMenu("&Ajustar Imagem")
        self.menutransparencia = self.barrademenu.addMenu("&Transparência")
        self.menusobre = self.barrademenu.addMenu("&Sobre")

        #actions
        self.opcaoabrir = self.menuarquivo.addAction("Abrir")
        self.opcaoabrir.triggered.connect(self.open_file)
        self.opcaoabrir.setShortcut("Ctrl+A")
        self.opcaoabrir.setCheckable(True)
        self.opcaoabrir.setChecked(True)

        self.menuarquivo.addSeparator()
        self.opcaosalvar = self.menuarquivo.addAction("Salvar como")
        self.opcaosalvar.triggered.connect(self.close)

        self.menuarquivo.addSeparator()
        self.opcaofechar = self.menuarquivo.addAction("Fechar")
        self.opcaofechar.setShortcut("Ctrl+x")
        self.opcaofechar.triggered.connect(self.close)

        self.opcaonegativa = self.menuTransformar.addAction("Negativa")
        self.opcaonegativa.triggered.connect(self.negativa_me)
        self.opcaonegativa.setShortcut("Ctrl+T")
        self.opcaonegativa.setCheckable(True)
        self.opcaonegativa.setChecked(True)

        self.opcaogamma = self.menuTransformar.addAction("Gamma")
        self.opcaogamma.triggered.connect(self.gamma_me)
        self.opcaogamma.setShortcut("Ctrl+G")
        self.opcaogamma.setCheckable(True)
        self.opcaogamma.setChecked(True)

        self.opcaoblur = self.menuTransformar.addAction("Blur")
        self.opcaoblur.triggered.connect(self.blur_me)
        self.opcaoblur.setShortcut("Ctrl+B")
        self.opcaoblur.setCheckable(True)
        self.opcaoblur.setChecked(True)

        self.menuTransformar.addSeparator()
        self.opcaocontour = self.menuTransformar.addAction("Contour")
        self.opcaocontour.triggered.connect(self.contour_me)
        self.opcaocontour.setShortcut("Ctrl+C")
        self.opcaocontour.setCheckable(True)
        self.opcaocontour.setChecked(True)

        self.menuTransformar.addSeparator()
        self.opcaosharpen = self.menuTransformar.addAction("Sharpen")
        self.opcaosharpen.triggered.connect(self.sharpen_me)
        self.opcaosharpen.setShortcut("Ctrl+S")
        self.opcaosharpen.setCheckable(True)
        self.opcaosharpen.setChecked(True)

        self.menuTransformar.addSeparator()
        self.opcaodetail = self.menuTransformar.addAction("Detail")
        self.opcaodetail.triggered.connect(self.detail_me)
        self.opcaodetail.setShortcut("Ctrl+D")
        self.opcaodetail.setCheckable(True)
        self.opcaodetail.setChecked(True)

        self.menuTransformar.addSeparator()
        self.opcaoedge = self.menuTransformar.addAction("Edge enhance")
        self.opcaoedge.triggered.connect(self.edge_me)
        self.opcaoedge.setCheckable(True)
        self.opcaoedge.setChecked(True)

        self.menuTransformar.addSeparator()
        self.opcaoedgem = self.menuTransformar.addAction("Edge enhance more")
        self.opcaoedgem.triggered.connect(self.edgeMore_me)
        self.opcaoedgem.setCheckable(True)
        self.opcaoedgem.setChecked(True)

        self.menuTransformar.addSeparator()
        self.opcaoemboss = self.menuTransformar.addAction("Emboss")
        self.opcaoemboss.triggered.connect(self.emboss_me)
        self.opcaoemboss.setCheckable(True)
        self.opcaoemboss.setChecked(True)

        self.menuTransformar.addSeparator()
        self.opcaofind = self.menuTransformar.addAction("Find")
        self.opcaofind.triggered.connect(self.find_me)
        self.opcaofind.setCheckable(True)
        self.opcaofind.setChecked(True)

        self.menuTransformar.addSeparator()
        self.opcaosmooth = self.menuTransformar.addAction("Smooth")
        self.opcaosmooth.triggered.connect(self.smooth_me)
        self.opcaosmooth.setCheckable(True)
        self.opcaosmooth.setChecked(True)

        self.menuTransformar.addSeparator()
        self.opcaosmoothm = self.menuTransformar.addAction("Smooth more")
        self.opcaosmoothm.triggered.connect(self.smoothMore_me)
        self.opcaosmoothm.setCheckable(True)
        self.opcaosmoothm.setChecked(True)
        
        self.menuTransformar.addSeparator()
        self.opcaoborda = self.menuTransformar.addMenu("Detecção de Bordas")
        self.opcaoborda1 = self.opcaoborda.addAction("Bordas 01")
        self.opcaoborda1.triggered.connect(self.filtro1_me)
        self.opcaoborda1.setCheckable(True)
        self.opcaoborda1.setChecked(True)

        self.opcaoborda.addSeparator()
        self.opcaoborda2 = self.opcaoborda.addAction("Bordas 02")
        self.opcaoborda2.triggered.connect(self.filtro2_me)
        self.opcaoborda2.setCheckable(True)
        self.opcaoborda2.setChecked(True)

        self.opcaoborda.addSeparator()
        self.opcaoborda3 = self.opcaoborda.addAction("Bordas 03")
        self.opcaoborda3.triggered.connect(self.filtro3_me)
        self.opcaoborda3.setCheckable(True)
        self.opcaoborda3.setChecked(True)

        self.menuTransformar.addSeparator()
        self.opcaocamadas = self.menuTransformar.addMenu("Camadas")
        self.opcaocamadar = self.opcaocamadas.addAction("Camada R")
        self.opcaocamadar.triggered.connect(self.Rcamada)
        self.opcaocamadar.setCheckable(True)
        self.opcaocamadar.setChecked(True)

        self.opcaocamadas.addSeparator()
        self.opcaocamadag = self.opcaocamadas.addAction("Camada G")
        self.opcaocamadag.triggered.connect(self.Gcamada)
        self.opcaocamadag.setCheckable(True)
        self.opcaocamadag.setChecked(True)

        self.opcaocamadas.addSeparator()
        self.opcaocamadab = self.opcaocamadas.addAction("Camada B")
        self.opcaocamadab.triggered.connect(self.Bcamada)
        self.opcaocamadab.setCheckable(True)
        self.opcaocamadab.setChecked(True)

        self.opcaoajuste = self.menuajustes.addMenu("Ajustar Imagem")
        self.opcaoespelharh = self.opcaoajuste.addAction("Espelhar Horizontalmente")
        self.opcaoespelharh.triggered.connect(self.espelhar_H)
        self.opcaoespelharh.setShortcut("Ctrl+H")
        self.opcaoespelharh.setCheckable(True)
        self.opcaoespelharh.setChecked(True)

        self.opcaoajuste.addSeparator()
        self.opcaoespelharv = self.opcaoajuste.addAction("Espelhar Verticalmente")
        self.opcaoespelharv.triggered.connect(self.espelhar_V)
        self.opcaoespelharv.setShortcut("Ctrl+N")
        self.opcaoespelharv.setCheckable(True)
        self.opcaoespelharv.setChecked(True)

        self.opcaoajuste.addSeparator()
        self.opcaorotacionarn = self.opcaoajuste.addAction("Rotacionar 90")
        self.opcaorotacionarn.triggered.connect(self.rotacionar_N)
        self.opcaorotacionarn.setCheckable(True)
        self.opcaorotacionarn.setChecked(True)

        self.opcaoajuste.addSeparator()
        self.opcaorotacionarc = self.opcaoajuste.addAction("Rotacionar 180")
        self.opcaorotacionarc.triggered.connect(self.rotacionar_C)
        self.opcaorotacionarc.setCheckable(True)
        self.opcaorotacionarc.setChecked(True)
        
        self.opcaoajuste.addSeparator()
        self.opcaorotacionard = self.opcaoajuste.addAction("Rotacionar 270")
        self.opcaorotacionard.triggered.connect(self.rotacionar_D)
        self.opcaorotacionard.setCheckable(True)
        self.opcaorotacionard.setChecked(True)

        self.opcaotransparencia = self.menutransparencia.addAction("Transparência")
        self.opcaotransparencia.triggered.connect(self.transparencia)
        self.opcaotransparencia.setShortcut("Ctrl+P")
        self.opcaotransparencia.setCheckable(True)
        self.opcaotransparencia.setChecked(True)

        self.opcaosobre = self.menusobre.addAction("Sobre o aplicativo")
        self.opcaosobre.triggered.connect(self.exibe_mensagem)
        self.opcaosobre.setCheckable(True)
        self.opcaosobre.setChecked(True)

        self.opcaoajuste.addSeparator()
        self.opcaosobre = self.menusobre.addAction("Sobre a imagem")
        self.opcaosobre.triggered.connect(self.sobre_imagem)
        self.opcaosobre.setCheckable(True)
        self.opcaosobre.setChecked(True)

        #widgets
        #Qlabel TEXTO
        self.texto = QLabel("Processamento Digital de Imagens", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        # Qlabel Imagem
        self.imagem1 = QLabel(self)
        self.endereco1 = 'images/natureza.jpg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        self.imagem2 = QLabel(self)
        self.endereco2 = 'images/natureza.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        # Organização
        self.layout.addWidget(self.texto, 0, 0, 1, 2)
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.setRowStretch(0,0)
        self.layout.setRowStretch(1,1)
        self.layout.setRowStretch(2,0)

    # metodos 
    def exibe_mensagem(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Desenvolvido por Guilherme Pereira da Silva e Arthur Pelizaro")
        self.msg.setWindowTitle("Sobre")
        self.msg.setInformativeText("Araraquara, 01/07/2021")
        self.msg.setDetailedText("Descrição: Aplicativo de processamento digital de imagens")
        self.msg.exec_()
        self.reply = self.msg.clickedButton()

    def sobre_imagem(self):
        self.msg2 = QMessageBox()
        self.msg2.setIcon(QMessageBox.Information)
        self.msg2.setText(self.endereco1)
        self.msg2.setWindowTitle("Sobre")
        self.msg2.setInformativeText("Altura 400\n Largura 400")
        self.msg2.exec_()
        self.reply = self.msg2.clickedButton()

    def open_file(self) :
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption='Open Image', directory=QtCore.QDir.currentPath(),
        filter='All Files (*.*);; Images (*.jpeg; *.png; *.jpg)', initialFilter='All Files (*.*)')
        print (fileName)
        if fileName != ' ':
            self.endereco1= fileName
            self.pixmap1 = QtGui.QPixmap(self.endereco1)
            self.pixmap1 = self.pixmap1.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.imagem1.setPixmap(self.pixmap1)
    #Filtros
    def negativa_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\ Negativa.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def gamma_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Gamma.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def blur_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Blur.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def contour_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Contour.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def sharpen_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Sharpen.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def detail_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Detail.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def edge_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\E_enhance.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def edgeMore_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\E_enhance_m.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def emboss_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Emboss.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def find_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Find.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def smooth_me(self):
        self.entrada = self.endereco1
        self.saida = '/images/Arquivo.jpg'
        self.script = '.\Smooth.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def smoothMore_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Smooth_m.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def filtro1_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Filtro01.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def filtro2_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Filtro02.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def filtro3_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Filtro03.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def escala_me(self):
        self.entrada = self.endereco1
        self.saida = 'images\Arquivo.jpg'
        self.script = '.\Escala.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        
    #Espelhar
    def espelhar_H(self):
        self.entrada = self.endereco1
        self.saida = 'images\espelhadoH.jpg'
        self.script = '.\EspelharH.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def espelhar_V(self):
        self.entrada = self.endereco1
        self.saida = 'images\espelhadoV.jpg'
        self.script = '.\EspelhadoV.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    #Rotacionar
    def rotacionar_N(self):
        self.entrada = self.endereco1
        self.saida = 'images\Rotacionado.jpg'
        self.script = '.\Rotacionar90.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def rotacionar_C(self):
        self.entrada = self.endereco1
        self.saida = 'images\Rotacionado.jpg'
        self.script = '.\Rotacionar180.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
    
    def rotacionar_D(self):
        self.entrada = self.endereco1
        self.saida = 'images\Rotacionado.jpg'
        self.script = '.\Rotacionar270.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    #Transparencia
    def transparencia (self):
        self.entrada = self.endereco1
        self.saida = 'images\Transparencia.png'
        self.script = '.\Transparencia.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    #Camadas
    def Rcamada (self):
        self.entrada = self.endereco1
        self.saida = 'images\camadaR.jpg'
        self.script = '.\R-camadas.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def Gcamada (self):
        self.entrada = self.endereco1
        self.saida = 'images\camadaG.jpg'
        self.script = '.\G-camadas.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def Bcamada (self):
        self.entrada = self.endereco1
        self.saida = 'images/camadaB.jpg'
        self.script = '.\B-camadas.py'
        self.program = 'python ' + self.script + ' \"' + self.entrada + '\" ' + self.saida
        print(self.program)
        subprocess.run(self.program, shell=True)

        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(400, 400, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

def window() :
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    
window()