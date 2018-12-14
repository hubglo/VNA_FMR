import visa
import time


class Gaussmeter:
    def __init__(self):
        address = 'TCPIP0::ifm118.ifmpan.poznan.pl::gpib0,12::INSTR'
        self.rm = visa.ResourceManager()
        self.inst = self.rm.open_resource(address)

    def Setup(self):
        self.inst.write('RST')

        self.inst.write("RANGE 4")

        self.inst.write("RDGMODE 1,2,1,1,1")

        self.inst.write("UNIT 1")

    def __del__(self):
        self.inst.close
        self.rm.close

    def SetVoltage(self,volt):
       self. inst.write("ANALOG 3,1,0.000E-3,00.000E-3,"+str(volt)+",10")
        
    def ReadField(self):
        return self.inst.query("RDGFIELD?")
        time.sleep(0.05)

gm=Gaussmeter()
gm.Setup()

print(gm.ReadField())

del gm
