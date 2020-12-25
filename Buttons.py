from PyQt5 import QtCore, QtGui, QtWidgets
import config as cg


class buttons:
    
    def __init__(self,cw,cwd):
        self.centralwidget = cw
        self.cwd = cwd
        self.button1()
        self.button2()
        self.button3()
        self.button4()
        self.button5()
        self.button6()
        self.button7()
        self.button8()
    
            
    def button1(self): #on - off
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(cg.button1_x, cg.button1_y, cg.button1_width, cg.button1_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.push_button), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.button1.setIcon(icon)
        self.button1.setIconSize(QtCore.QSize(cg.button1_width, cg.button1_height))
        self.button1.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button1.setCheckable(False)
        self.button1.setEnabled(True)
        self.button1.setObjectName("push_button")
        # self.button1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
    def button2(self): # reconnect commPorts
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(cg.button2_x,cg.button2_y, cg.button2_width, cg.button2_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.refresh), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button2.setIcon(icon)
        self.button2.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button2.setIconSize(QtCore.QSize(cg.button2_width, cg.button2_height))
        self.button2.setCheckable(False)
        self.button2.setEnabled(True)
        self.button2.setObjectName("refresh")
        
    def button3(self): # goto settings tab
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(cg.button3_x,cg.button3_y, cg.button2_width, cg.button2_height))
        # font = QtGui.QFont()
        # font.setFamily("Microsoft Tai Le")
        # font.setPointSize(14)
        # font.setBold(True)
        # font.setUnderline(True)
        # font.setWeight(75)
        # font.setStrikeOut(False)
        # self.button3.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.settings), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button3.setIcon(icon)
        self.button3.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button3.setIconSize(QtCore.QSize(cg.button3_width, cg.button3_height))
        self.button3.setCheckable(False)
        self.button2.setEnabled(True)
        self.button3.setObjectName("settings")
    
    def button4(self): # go back
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(cg.button4_x,cg.button4_y, cg.button4_width, cg.button4_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.goBack), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button4.setIcon(icon)
        self.button4.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button4.setIconSize(QtCore.QSize(cg.button4_width, cg.button4_height))
        self.button4.setEnabled(False)
        self.button4.setCheckable(False)
        self.button4.hide()
        self.button4.setObjectName("go back")

    def button5(self): # show credits
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(cg.button3_x,cg.button3_y, cg.button2_width, cg.button2_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.credits), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button5.setIcon(icon)
        self.button5.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button5.setIconSize(QtCore.QSize(cg.button5_width, cg.button5_height))
        self.button5.setCheckable(False)
        self.button5.setEnabled(False)
        self.button5.hide()
        self.button5.setObjectName("credits")
        
    def button6(self): # show available comports
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(cg.button1_x+10,cg.button1_y-50, cg.button6_width, cg.button6_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.commPort), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button6.setIcon(icon)
        self.button6.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button6.setIconSize(QtCore.QSize(cg.button6_width, cg.button6_height))
        self.button6.setCheckable(False)
        self.button6.setEnabled(False)
        self.button6.hide()
        self.button6.setObjectName("commPorts")
     
    def button7(self): # show display settings
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(cg.button1_x+10,cg.button1_y+100, cg.button6_width, cg.button6_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.display), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button7.setIcon(icon)
        self.button7.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button7.setIconSize(QtCore.QSize(cg.button6_width, cg.button6_height))
        self.button7.setCheckable(False)
        self.button7.setEnabled(False)
        self.button7.hide()
        self.button7.setObjectName("display") 

    def button8(self): # change comm port
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(cg.button3_x-5,cg.button3_y-5, cg.button8_width, cg.button8_height))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.cwd+"/"+cg.newUsb), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button8.setIcon(icon)
        self.button8.setStyleSheet("border-radius : 50; border : .1px solid black")
        self.button8.setIconSize(QtCore.QSize(cg.button8_width, cg.button8_height))
        self.button8.setCheckable(False)
        self.button8.setEnabled(False)
        self.button8.hide()
        self.button8.setObjectName("changeCommPort") 
        
    