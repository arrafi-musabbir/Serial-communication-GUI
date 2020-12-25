from PyQt5 import QtCore, QtGui, QtWidgets
import config as cg 

class grapics:
    
    def __init__(self,cw,cwd,sc):
        self.sc = sc
        self.serial = 0
        self.centralwidget = cw
        self.cwd = cwd
        self.background()
        self.indicator()
        self.status()
        self.green_ring()
        self.logo()
        self.click_to()
        
    
    def background(self):
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, cg.width, cg.height))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.background.setFont(font)
        self.background.setAutoFillBackground(False)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.background))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
                      
    def indicator(self):
        
        self.indicator = QtWidgets.QLabel(self.centralwidget)
        self.indicator.setGeometry(QtCore.QRect(cg.indicator_x,cg.indicator_y, cg.indicator_width, cg.indicator_height))
        self.indicator.setText("")
        self.indicator.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.red_indicator))
        self.indicator.setScaledContents(True)
        self.indicator.setObjectName("indicator")
        self.indicator.show()
        
    def status(self):
        
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(cg.width//2.7, cg.height//1.6, 11, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(60)
        font.setBold(True)
        font.setWeight(75)
        self.status.setText("STATUS  <font color=\"red\"> OFF </font> ")
        self.status.setFont(font)
        self.status.setStyleSheet("color:rgb(255, 255, 255)")
        self.status.setScaledContents(True)
        self.status.setObjectName("status")
        self.status.adjustSize()

    def green_ring(self):
        
        self.ring = QtWidgets.QLabel(self.centralwidget)
        self.ring.setGeometry(QtCore.QRect(cg.button1_x-5, cg.button1_y-5 , 130, 130))
        self.ring.setText(" ")
        self.ring.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.green_ring))
        self.ring.setScaledContents(True)
        self.ring.setObjectName("rign")
        self.ring.setEnabled(False)
        
    def logo(self):
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(cg.width//1.20,cg.height//1.10, cg.logo_width, cg.logo_height))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.logo))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

    def click_to(self):
        self.click_to = QtWidgets.QLabel(self.centralwidget)
        self.click_to.setGeometry(QtCore.QRect(cg.width//2.7, cg.height-cg.height//3.5, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(24)
        font.setWeight(75)
        self.click_to.setFont(font)
        self.click_to.setText("CLICK SPACE TO SWITCH ON")
        self.click_to.setStyleSheet("color:rgb(255, 255, 255)")
        self.click_to.setObjectName("click_to")
        self.click_to.setAlignment(QtCore.Qt.AlignCenter)
        self.click_to.adjustSize()

    def connectedport(self):
        self.port = str(self.sc.connectedPort).upper()
        self.selectedPort = QtWidgets.QLabel(self.centralwidget)
        self.selectedPort.setGeometry(QtCore.QRect(cg.width//2.8, cg.height//1.4 - 40, 10, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(24)
        font.setWeight(75)
        self.selectedPort.setText("CONNECTED PORT:"+self.port)
        self.selectedPort.setFont(font)
        self.selectedPort.setStyleSheet("color:rgb(255, 255, 0)")
        self.selectedPort.setScaledContents(True)
        self.selectedPort.setObjectName("selectedPort")
        self.selectedPort.hide()
        self.selectedPort.adjustSize()

    def availablePorts(self):
        self.ports = self.sc.find_com_port()
        self.showPorts = QtWidgets.QLabel(self.centralwidget)
        self.showPorts.setGeometry(QtCore.QRect(cg.width//2.3, cg.height//2.3,  cg.button6_width, cg.button6_height))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.showPorts.setFont(font)
        self.showPorts.setStyleSheet("color:rgb(255, 255, 255)")
        self.showPorts.setText("AVAILABLE PORTS:\n" +str(self.ports).upper())
        self.showPorts.setAlignment(QtCore.Qt.AlignCenter)
        if self.ports is None:
            self.showPorts.setText("AVAILABLE PORTS:\n"+" "+"NONE")
        self.showPorts.adjustSize()
        self.showPorts.hide()
        self.showPorts.setObjectName("showPorts")
        
    def portIndicator(self):
        
        self.portIndicator = QtWidgets.QLabel(self.centralwidget)
        self.portIndicator.setGeometry(QtCore.QRect(cg.width-50, 20, 25,25))
        self.portIndicator.setText("")
        self.portIndicator.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.noUsb))
        self.portIndicator.setScaledContents(True)
        self.portIndicator.setObjectName("portIndicator")

    def showCredits(self):
        self.credits = QtWidgets.QLabel(self.centralwidget)
        self.credits.setGeometry(QtCore.QRect(cg.width//2.8, cg.height/2, 11, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        name = "MUSABBIR AHMED ARRAFI"
        email = "musabbir.arrafi@gmail.com"
        self.credits.setText(name+"\n"+email)
        self.credits.setFont(font)
        self.credits.setStyleSheet("color:rgb(255, 255, 255)")
        self.credits.setScaledContents(True)
        # self.credits.setStyleSheet("QLabel { background-color : black;color:rgb(255, 255, 255)}")
        self.credits.setObjectName("credits")
        self.credits.setAlignment(QtCore.Qt.AlignCenter)
        self.credits.adjustSize()