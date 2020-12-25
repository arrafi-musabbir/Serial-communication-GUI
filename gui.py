from PyQt5 import QtCore, QtGui, QtWidgets
from Serial_Comm import serialComm
import serial
import config as cg 
import time
import sys
import os
from Buttons import buttons
from Grapics import grapics


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        self.sc = serialComm()
        self.state = "Main"
        self.state_data = "off"
        self.cwd = os.getcwd()
        
        MainWindow.setObjectName("MainWindow")
        
        MainWindow.setGeometry(0,0,cg.width, cg.height)
        MainWindow.setEnabled(True)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.grapics = grapics(self.centralwidget,self.cwd,self.sc)
        self.buttons = buttons(self.centralwidget,self.cwd)
        
        self.actionExit = QtWidgets.QShortcut(QtGui.QKeySequence('Esc'),MainWindow)
        self.actionExit.activated.connect(self.action_Exit)
        
        self.actionSwitch = QtWidgets.QShortcut(QtGui.QKeySequence('Space'),MainWindow)
        self.actionSwitch.activated.connect(self.action_Switch)
            
            
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.buttons.button1.clicked.connect(self.button1_click)
        self.buttons.button2.clicked.connect(self.button2_click)
        self.buttons.button3.clicked.connect(self.button3_click)
        self.buttons.button4.clicked.connect(self.button4_click)
        self.buttons.button5.clicked.connect(self.button5_click)
        self.buttons.button6.clicked.connect(self.button6_click)
        self.buttons.button8.clicked.connect(self.button8_click)
    
    def action_Switch(self):
        if self.state == "Main":
            self.button1_click()
        elif self.state == "showCommPorts":
            self.button8_click()
        
    def action_Exit(self):
        if self.state == "Settings":
            self.loadMain()
        elif self.state == "showCommPorts":
            self.goto_settings()
        elif self.state == "credits":
            self.goto_settings()
        else:
            # print("Going offline")
            # time.sleep(1)
            self.offline()
            # print("Exiting...")
            time.sleep(1)
            # print("...")
            sys.exit()
        
    def goto_settings(self):
        if self.state == "Main":
            self.actionSwitch.disconnect()
            self.grapics.indicator.hide()
            self.buttons.button1.hide()
            self.buttons.button1.setEnabled(False)
            self.buttons.button2.hide()
            self.buttons.button2.setEnabled(False)
            self.buttons.button3.hide()
            self.buttons.button3.setEnabled(False)
            self.grapics.status.hide() 
            self.grapics.ring.hide()
            self.grapics.click_to.hide()
        elif self.state == "showCommPorts":
            self.actionSwitch.disconnect()
            self.grapics.showPorts.setEnabled(False)
            self.grapics.showPorts.hide()
            self.grapics.selectedPort.hide()
            self.grapics.selectedPort.hide()
            self.buttons.button8.hide()
            self.buttons.button8.setEnabled(False)
            self.grapics.click_to.hide()
        elif self.state == "credits":
            self.grapics.credits.hide()
            
        self.blur_effect = QtWidgets.QGraphicsBlurEffect() 
        self.grapics.background.setGraphicsEffect(self.blur_effect)
       
        self.buttons.button4.show()
        self.buttons.button4.setEnabled(True)
        self.buttons.button5.show()
        self.buttons.button5.setEnabled(True)
        self.buttons.button6.show()
        self.buttons.button6.setEnabled(True)
        self.buttons.button7.show()
        self.buttons.button7.setEnabled(True)
        
        self.state = "Settings"
           
    def loadMain(self):
        if self.sc.connectedPort is not None:
                self.grapics.ring.setEnabled(True)
        self.blur_effect.setEnabled(False)
        self.grapics.indicator.show()
        self.buttons.button1.show()
        self.buttons.button1.setEnabled(True)
        self.buttons.button2.show()
        self.buttons.button2.setEnabled(True)
        self.buttons.button3.show()
        self.buttons.button3.setEnabled(True)
        self.buttons.button4.hide()
        self.buttons.button4.setEnabled(False)
        self.buttons.button5.hide()
        self.buttons.button5.setEnabled(False)
        self.buttons.button6.hide()
        self.buttons.button6.setEnabled(False)
        self.buttons.button7.hide()
        self.buttons.button7.setEnabled(False)
        self.actionSwitch.activated.connect(self.action_Switch)
        self.grapics.status.show()
        self.grapics.ring.show()
        self.grapics.click_to.show()
        self.grapics.click_to.setText("CLICK SPACE TO SWITCH ON")
        self.grapics.click_to.adjustSize()
        self.state = "Main"
    
    def gotoCommPorts(self):
        self.state = "showCommPorts"
        self.actionSwitch.activated.connect(self.action_Switch)
        self.buttons.button4.show()
        self.buttons.button4.setEnabled(True)
        self.buttons.button5.hide()
        self.buttons.button5.setEnabled(False)
        self.buttons.button6.hide()
        self.buttons.button6.setEnabled(False)
        self.buttons.button7.hide()
        self.buttons.button7.setEnabled(False)
        self.buttons.button8.show()
        self.buttons.button8.setEnabled(True)
        self.grapics.availablePorts()
        self.grapics.showPorts.show()
        self.grapics.connectedport()
        self.grapics.selectedPort.show()
        self.grapics.click_to.setText("CLICK SPACE TO SWITCH PORTS")
        self.grapics.click_to.show()
        self.grapics.click_to.adjustSize()

    def button1_click(self):
        if  self.state_data == "off":
            self.state_data = "on"
            self.online()
            print("ONLINE")
        elif  self.state_data == "on":
            self.state_data = "off"
            self.offline()
            print("OFFLINE")
        # time.sleep(1)
        
    def button2_click(self):  
        self.grapics.click_to.adjustSize()
        try:
            self.sc.auto_establish_comm()
            time.sleep(.5)
            if self.sc.connectedPort is not None:
                self.grapics.ring.setEnabled(True)
            else:
                self.grapics.ring.setEnabled(False)
        except serial.serialutil.SerialException:
            pass
            # print("Communication port already established")
       
        
    def button3_click(self):
        self.goto_settings()
    
    def button4_click(self):
        if self.state == "Settings":
            self.loadMain()
        elif self.state == "showCommPorts":
            self.goto_settings()
        elif self.state == "credits":
            self.goto_settings()
    
    def button6_click(self):
        self.gotoCommPorts()

    def button5_click(self):
        self.state = "credits"
        self.buttons.button4.show()
        self.buttons.button4.setEnabled(True)
        self.buttons.button5.hide()
        self.buttons.button5.setEnabled(False)
        self.buttons.button6.hide()
        self.buttons.button6.setEnabled(False)
        self.buttons.button7.hide()
        self.buttons.button7.setEnabled(False)
        self.grapics.showCredits()
        self.grapics.credits.show()
    
    def button8_click(self):
        self.offline()
        self.sc.change_comPort()
        self.grapics.click_to.setText("CLICK SPACE TO SWITCH PORTS")
        self.grapics.click_to.show()
        self.grapics.click_to.adjustSize()
        self.grapics.selectedPort.setText("CONNECTED PORT:"+str(self.sc.connectedPort).upper())
        self.grapics.showPorts.setText("AVAILABLE PORTS:\n"+str(self.sc.find_com_port()).upper())
        self.grapics.selectedPort.adjustSize()
        self.grapics.showPorts.adjustSize()
        if self.sc.connectedPort is None:
            self.grapics.ring.setEnabled(False)

    def online(self):
        if self.sc.connection == 1:
            if self.sc.communicate(self.state_data) == False:
                self.grapics.ring.setEnabled(False)
        time.sleep(.5)
        self.grapics.status.setText("STATUS  <font color=\"green\"> ON </font> ")
        self.grapics.status.adjustSize() 
        self.grapics.click_to.setText("CLICK SPACE TO SWITCH OFF")
        self.grapics.click_to.adjustSize()
        self.grapics.indicator.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.green_indicator))
        
    def offline(self):
        self.state_data = "off"
        if self.sc.connection == 1:
            if self.sc.communicate(self.state_data) == False:
                self.grapics.ring.setEnabled(False)
        time.sleep(.5)
        self.grapics.status.setText("STATUS  <font color=\"red\"> OFF </font> ")
        self.grapics.status.adjustSize() 
        self.grapics.click_to.setText("CLICK SPACE TO SWITCH ON")
        self.grapics.indicator.setPixmap(QtGui.QPixmap(self.cwd+"/"+cg.red_indicator))
        
    
        

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.showNormal()
    sys.exit(app.exec_())
