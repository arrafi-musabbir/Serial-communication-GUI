import serial, time
import serial.tools.list_ports

class serialComm():
    
    def __init__(self):
        self.commPort = None
        self.connection = 0
        self.listPorts = list()
        self.connectedPort = None
        
    def auto_establish_comm(self):
        self.find_com_port()
        if self.commPort is not None:
            self.connectedPort = self.commPort
            # print(self.connectedPort)
            # print("Communication port found: ",self.connectedPort)
            try:
                self.serialcom = serial.Serial(self.connectedPort, 9600)
                # print("Establishing communication at port: ",self.connectedPort)
                self.serialcom.timeout = 1
                self.connection = 1
            except serial.serialutil.SerialException:
                        self.serialcom.close()
        else:
            self.connectedPort = None
            self.connection = 0
            # print("No communication port found")

    def change_comPort(self):
        if self.connectedPort is None:
            self.auto_establish_comm()
        else:
            self.find_com_port()
            if len(self.listPorts)>1:
                try:
                    # self.serialcom.close()
                    index = self.listPorts.index(self.connectedPort)
                    if len(self.listPorts) == (index+1):
                        index = -1
                    self.connectedPort = self.listPorts[index+1]
                    # print("New Communication port selected: ",self.connectedPort)
                    try:
                        self.serialcom = serial.Serial(self.connectedPort, 9600)
                        # print("Establishing communication at new port: ",self.connectedPort)
                        self.serialcom.timeout = 1
                        self.connection = 1
                        time.sleep(.5)
                    except serial.serialutil.SerialException:
                        self.serialcom.close()
                    
                except ValueError:
                    self.connectedPort = None
            elif len(self.listPorts) == 1:
                self.connectedPort = self.listPorts[0]
            else:
                self.connectedPort = None
                self.connection = 0
                # print("No new communication port found")
            
            
    def find_com_port(self):
        self.listPorts.clear()
        portData = serial.tools.list_ports.comports()
        if len(portData)>0:
            for i in portData:
                port = str(i).split()
                self.listPorts.append(port[0])
            # print(self.listPorts)
            try:
                self.listPorts.remove('/dev/ttyAMA0')
            except ValueError:
                pass
            if len(self.listPorts)>0:
                self.commPort = self.listPorts[0]
                return self.listPorts
            else:
                self.commPort = None
                return None
        else:
            self.commPort = None
            return None
        
    def communicate(self,data):
        try:
            self.serialcom.write(data.encode())
            time.sleep(0.5)
            return True
        except serial.serialutil.SerialException:
            # print("Communication port disconnected")
            return False
        
        
        
if __name__ == "__main__":
    a = serialComm()
    print(a.find_com_port())
    
