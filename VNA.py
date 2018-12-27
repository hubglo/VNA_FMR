import visa
import matplotlib
import matplotlib.pyplot as plt


class VNA:
    def __init__(self):
        address = 'TCPIP0::150.254.221.118::hpib7,16::INSTR'
        self.rm = visa.ResourceManager()
        self.inst = self.rm.open_resource(address)

    def Setup(self):
        self.inst.write("*RST")
        self.inst.write("*CLS")
        self.inst.write("CALCulate:PARameter:DELete:ALL")


        self.inst.write("CALCulate:PARameter:SELect 'CH1_S11_1'")
        
        
        self.inst.write("SENSe1:SWEep:POIN 10")
        # 'Turn continuous sweep off
        self.inst.write("INITiate:CONTinuous OFF")

    def __del__(self):
        self.inst.close()
        self.rm.close()

    def TakeASweep(self):
        # 'Take a sweep
        self.inst.write("INITiate:IMMediate;*wai")
        
    def ReadComplex(self):
        complex_values_str=self.inst.query("CALCulate:DATA? SDATA") #'Corrected, Complex Meas
        dane_complex=[float(i) for i in complex_values_str[:-1].split(',')]
        # print(dane_complex)
        Re=dane_complex[0::2]
        Im=dane_complex[1::2]
        return [Re,Im]


# print(inst.query("CALCulate1:PARameter:CATalog?"))
# print(inst.query("DISPlay:CATalog?"))
# print(inst.query("DISPlay:WINDow1:CATalog?"))
# values=inst.query("CALCulate:DATA? FDATA")
# dane=[float(i) for i in values[:-1].split(',')]

if __name__ == "__main__":
    vna=VNA()
    vna.Setup()
    vna.TakeASweep()
    dane=vna.ReadComplex()

    fig, ax = plt.subplots()


    ax.plot(dane[0])
    ax.plot(dane[1])

    ax.set(xlabel='points', ylabel='Signal (a.u.)',
        title='Signal from VNA')
    ax.grid()

    # fig.savefig("test.png")
    plt.show()

    del vna




